<template>
  <Header />
  <div id="main-content">
      <div id="load-gif">
        <img src="../assets/gifs/load.gif">
      </div>
      <div id="profile-info">
        <table class="fl-table fl-profile">
            <thead>
                <tr>
                    <th colspan="2">Информация о пользователе</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Фамилия</td>
                    <td>{{ surname }}</td>
                </tr>
                <tr>
                    <td>Имя</td>
                    <td>{{ name }}</td>
                </tr>
                <tr>
                    <td>Отчество</td>
                    <td>{{ patronymic }}</td>
                </tr>
                <tr>
                    <td>Подразделение</td>
                    <td>{{ department }}</td>
                </tr>
                <tr>
                    <td>Должность</td>
                    <td>{{ position }}</td>
                </tr>
                <tr>
                    <td>Телефон</td>
                    <td>{{ phone }}</td>
                </tr>
                <tr>
                    <td>Email</td>
                    <td>{{ email }}</td>
                </tr>
            </tbody>
        </table>
      </div>
  </div>
</template>

<script>
import Header from "../components/Header.vue"

export default {
  name: 'Profile',
  components: {Header},
  data() {
    return {
        surname: '',
        name: '',
        patronymic: '',
        department: '',
        position: '',
        phone: '',
    }
  },
  methods:{
    getInfo() {
      fetch(this.$store.state.backendUrl+'/api/authen/profile/', {
      method: 'GET',
      headers: {
          'Authorization': 'Token '+localStorage.getItem('access_token'),
      },
      })
      .then(resp => {
        if (resp.status == 200) {
            return resp.json()
        } else {
           showBanner('.banner.error', 'Произошла ошибка, повторите попытку позже')
           return false
        }
      })
      .then(data => {
        this.surname = data.profile.surname;
        this.name = data.profile.name;
        this.patronymic = data.profile.patronymic;
        this.phone = data.profile.phone;
        this.department = data.profile.department;
        this.position = data.profile.position;
        this.email = data.email;
        $('#load-gif').css('display', 'none');
        $('#profile-info').css('display', 'block');
      })
    }
  },
  beforeMount(){
    this.getInfo()
  },
}
</script>

<style>
#load-gif{
  margin: 0 auto;
}
#profile-info{
  margin: 0 auto;
  display: none;
}
</style>
