import { createApp } from 'vue'
import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'

// Create a new store instance.
export default createStore({
  plugins: [createPersistedState({
        storage: window.localStorage,
  })],
  state: {
    backendUrl: process.env.BACKEND_URL,
    token: localStorage.getItem('access_token') || '',
    admin: localStorage.getItem('is_admin') || '',
    status: ''
  },
  actions: {
    AUTH_REQUEST ({commit, dispatch}, user ) {
    return new Promise((resolve, reject) => { // The Promise used for router redirect in login
      commit('AUTH_REQUEST');
      fetch(this.state.backendUrl+'/api/authen/login/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie("csrftoken"),
            'Content-Type': 'application/json;charset=UTF-8',
        },
        body: JSON.stringify({
            'login': user.username,
            'pass': user.pass
        })
      })
      .then(resp => resp.json())
      .then(data => {
          if ('error' in data){
            commit('AUTH_ERROR', data.error)
            showBanner('.banner.error', data.error)
          } else {
            const token = data.token
            commit('AUTH_SUCCESS', token)
            localStorage.setItem('access_token', token)
            fetch(this.state.backendUrl+'/api/authen/check_admin/', {
              method: 'GET',
              headers: {
                  'Authorization': 'Token '+localStorage.getItem('access_token'),
              },
              })
              .then(res => res.json())
              .then(data => {
                if (data.is_admin == true) {
                   localStorage.setItem('is_admin', true)
                   commit('AUTH_CHECKADMIN', true)
                } else {
                   localStorage.setItem('is_admin', false)
                   commit('AUTH_CHECKADMIN', false)
                }
                showBanner('.banner.success', 'Вход выполнен успешно');
                resolve();
              })
          }
        })
      .catch(err => {
        commit('AUTH_ERROR', err)
        localStorage.removeItem('access_token') // if the request fails, remove any possible user token if possible
        localStorage.removeItem('is_admin') // if the request fails, remove any possible user token if possible
        reject(err)
        showBanner('.banner.error', 'Неудачная попытка входа в систему. Поробуйте еще раз')
      })
      })

     },
    AUTH_LOGOUT ({commit, dispatch}) {
    return new Promise((resolve, reject) => {
      localStorage.removeItem('access_token') // clear your user's token from localstorage
      resolve()
    })
  }
  },
  mutations: {
      AUTH_REQUEST (state) {
        state.status = 'loading'
      },
      AUTH_SUCCESS (state, token, fio, profile_id) {
        state.status = 'success',
        state.token = token
      },
      AUTH_CHECKADMIN (state, is_admin) {
        state.admin = is_admin
      },
      AUTH_ERROR (state) {
        state.status = 'error'
      },
    },
  modules:{},
  getters:{
    getServerUrl: state => state.backendUrl,
    isAuthenticated: state => !!state.token,
    authStatus: state => state.status,
  }
})