import { createRouter, createWebHistory } from 'vue-router'
import Main from "../views/Main.vue";
import store from '../store/index.js';
import Sign from "../views/Sign.vue";
import Profile from "../views/Profile.vue"
import DocKinds from "../views/administrative/DocKinds.vue"
import DocTypes from "../views/administrative/DocTypes.vue"
import DocTypeCategories from "../views/administrative/DocTypeCategories.vue"
import DocRequisites from "../views/administrative/DocRequisites.vue"
import DocTemplates from "../views/administrative/templates/DocTemplates.vue"
import NewTemplate from "../views/administrative/templates/NewTemplate.vue"

const ifAuthenticated = (to, from, next) => {
  if (!(store.getters.isAuthenticated)) {
    showBanner('.banner.error', 'Пожалуйста, ввойдите в систему')
    next('/sign-in?nextUrl='+to.path)
    return
  } else {
    fetch(store.state.backendUrl+'/api/authen/check_auth/', {
      method: 'GET',
      headers: {
          'Authorization': 'Token '+localStorage.getItem('access_token'),
      },
    })
    .then(resp => {
      if (resp.status == 401 || resp.status == 403) {
        showBanner('.banner.error', 'Пожалуйста, авторизируйтесь')
        next('/sign-in?nextUrl='+to.path)
        return
      } else {
        next()
        return
      }
    })
  }
}

const isAdministrator = (to, from, next) => {
    if (store.state.admin == true) {
        next()
        return
    } else {
        showBanner('.banner.error', 'У вас нет доступа на просмотр данного раздела')
        next('/')
        return
    }
}

const routes = [
  {
    path: '/sign-in',
    name: 'SignIn',
    component: Sign,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
    beforeEnter: ifAuthenticated
  },
  {
    path: '/',
    name: 'Main',
    component: Main,
    beforeEnter: ifAuthenticated
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    beforeEnter: ifAuthenticated
  },
  {
    path: '/administrative/guides/doc_kinds',
    name: 'DocKinds',
    component: DocKinds,
    beforeEnter: [ifAuthenticated, isAdministrator]
  },
  {
    path: '/administrative/guides/doc_types',
    name: 'DocTypes',
    component: DocTypes,
    beforeEnter: [ifAuthenticated, isAdministrator]
  },
  {
    path: '/administrative/guides/doc_types',
    name: 'DocTypes',
    component: DocTypes,
    beforeEnter: [ifAuthenticated, isAdministrator]
  },
  {
    path: '/administrative/guides/doc_categories',
    name: 'DocTypeCategories',
    component: DocTypeCategories,
    beforeEnter: [ifAuthenticated, isAdministrator]
  },
  {
    path: '/administrative/guides/doc_requisites',
    name: 'DocRequisites',
    component: DocRequisites,
    beforeEnter: [ifAuthenticated, isAdministrator]
  },
  {
    path: '/administrative/guides/doc_templates',
    name: 'DocTemplates',
    component: DocTemplates,
    beforeEnter: [ifAuthenticated, isAdministrator]
  },
  {
    path: '/administrative/guides/new_template',
    name: 'NewTemplate',
    component: NewTemplate,
    beforeEnter: [ifAuthenticated, isAdministrator]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})


export default router
