<template>

    <div class="SignIn">
        <main class="form-signin w-25 m-auto">
          <form class="form-sign" @submit.prevent="login">
            <div class="form-elems-center">
                <img class="mb-4" src="../assets/logo.png" style="margin: 0 auto; width: 45%; height: 45%">
                <h1 class="h3 mb-3 fw-normal">СЭД ЦОПМКиМКО</h1>

                <div class="form-floating">
                  <input type="text" class="form-control w-75 m-auto" v-model="username" id="floatingInput" placeholder="Логин">
                </div>
                <div class="form-floating">
                  <input type="password" class="form-control w-75 m-auto" v-model="pass" id="floatingPassword" placeholder="Пароль">
                </div><br>
                <div id="div-login-button"></div><br>
                <button class="w-50 btn btn-lg btn-primary red-butt" id="login-button"
                    type="submit">Войти</button>
            </div>
          </form>
        </main>
    </div>
</template>

<script>
import LoadGif from "../assets/gifs/load.gif"

export default {
    methods:{
        RedirectToNext() {
           this.$router.push({ path: getUrlParameter('nextUrl') })
        },
        login: function() {
          var gif = '<img src="'+LoadGif+'" style="width:10%;height:10%">'
          $('#login-button').css('visibility', 'collapse');
          $('#div-login-button').append(gif);
          const { username, pass } = this;
           this.$store.dispatch('AUTH_REQUEST', { username, pass }).then(() => {
             if (getUrlParameter('nextUrl')) {
                this.$router.push({ path: getUrlParameter('nextUrl') })
             } else this.$router.push('/')
          })
          $('#div-login-button').empty();
          $('#login-button').css('visibility', 'visible');
        }
    }
}
</script>

<style>
.SignIn{
    background-color: #3a4058;
    color: white;
    width: 100vw;
    height: 100vh;
    display: flex;
    vertical-align: middle;
}
.form-elems-center{
    text-align:center;
    align-items:center;
    justify-content: center;
    vertical-align: middle;
}
.red-butt, .red-butt:hover{
    background-color: #ea544a;
    border-color: #ea544a;
}


@import '~bootstrap';
</style>