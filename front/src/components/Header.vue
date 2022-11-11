<template>
    <header class="p-3 mb-3 border-bottom main-header">
    <div class="container-nav">
      <div class="align-items-center justify-width">
        <div class="margin-left">
          СЭД ГАУ ИО ЦОПМКиМКО
        </div>
        <div class="margin-right">
            <div class="wrapper-menu"><ul class="main-menu">
              <li id="menu-item-1" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-4 current_page_item menu-item-1">
                  <router-link to="/">Главная</router-link></li>
                  <li id="menu-item-2" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-2">
                    Мои задания
                        <ul class="sub-menu">
                          <li id="menu-item-3" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3"><a href="/sample-page/">Создать</a></li>
                          <li id="menu-item-4" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4"><a href="/sample-page/">Входящие</a></li>
                          <li id="menu-item-5" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-5"><a href="/sample-page-2/">Исходящие</a></li>
                        </ul>
                  </li>
                  <li id="menu-item-6" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-6">
                    Мои документы
                        <ul class="sub-menu">
                          <li id="menu-item-7" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8"><a href="contact-us-2/our-location/">Создать</a></li>
                          <li id="menu-item-8" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8"><a href="contact-us-2/our-location/">Входящие</a></li>
                          <li id="menu-item-9" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-9"><a href="contact-us-2/our-location/">Исходящие</a></li>
                        </ul>
                  </li>
                  <li v-if="admin == true" id="menu-item-10" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-10">
                  Администрирование
                    <ul class="sub-menu">
                      <li id="menu-item-11" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-11"><a href="contact-us-2/our-location/">Пользователи</a></li>
                      <li id="menu-item-12" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-12">
                        <router-link to="/administrative/guides/doc_kinds">Справочники</router-link>
                      </li>
                      <li id="menu-item-13" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13"><a href="contact-us-2/our-location/">Журналы</a></li>
                    </ul>
                  </li>
                  <li id="menu-item-14" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-14">
                        Система
                    <ul class="sub-menu">
                      <li id="menu-item-15" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-15"><router-link to="/about">Настройки</router-link></li>
                      <li id="menu-item-16" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-16"><router-link to="/profile">Профиль</router-link></li>
                      <li id="menu-item-17" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-17">
                        <a href="#" v-on:click="logout">Выход</a>
                        </li>
                    </ul>
                  </li>
                  </ul>
              </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
    export default {
        name: "Header",
        data(){
          return {
            admin: this.$store.state.admin
          }
        },
        methods: {
          logout: function () {
            this.$store.dispatch('AUTH_LOGOUT')
            .then(() => {
              this.$router.push('/sign-in')
            })
          },
        }
    }
</script>

<style>
header{
  position: sticky;
  z-index: 15;
  width: 100vw;
  height: 75px;
  display: none;
  background-color: #373c59;
}
.container-nav{
  max-width:100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}
.justify-width{
  width: 100%;
  height: 35px;
  display:flex;
  vertical-align: middle;
  position: relative;
}
.margin-right{
  display: flex;
  position: absolute;
  right: 2.5vw;
  color: white;
  font-weight: bold;
}
.margin-left{
  display: flex;
  position: absolute;
  left: 0;
  color: white;
  font-weight: bold;
}
.wrapper-menu{
  background-color: #373c59;
  color: white;
}
.main-menu{
  text-align:left;
  display:inline-block;
  background-color:#373c59;
  color: white;
}
.main-menu a, .main-menu a:hover{
  color: white;
  background-color: #373c59;
  text-decoration:none
}
.main-menu{
  list-style:none;
  padding:0;
  margin:0;
  background-color: #373c59;
}
.main-menu li{
  color: white;
  display:block;
  padding:0;
  position:relative;
  vertical-align:middle;
  background-color: #373c59;
}
.main-menu > li{
  background-color:#373c59;
  color: white;
}
.main-menu > li > a{
  background-color: #373c59;
  display:block;
  padding:.75em 1.25em;
}
.main-menu ul.sub-menu{
  color: white;
  position:relative;
  padding:0
}
.main-menu ul.sub-menu li{
  display:block;
  color: white;
}
.main-menu ul.sub-menu a{
  background-color:#373c59;
  color:#fff;
  padding:.75em 1.25em;
  display:block
}
.main-menu > li:hover ul.sub-menu{
  background-color:#373c59;
  color:#fff;
}
.main-menu li{
  display:inline-block;
}
.main-menu > li > a{
  display:block;}
.main-menu > li > a:hover{
  background-color:#f15c4e;
  color:#fff;
}
.main-menu > li:hover ul.sub-menu, .main-menu > li:focus ul.sub-menu{
  visibility: visible;
  opacity:1
}
.main-menu > li.menu-item-has-children{
  padding-right:1.5em;
  overflow:hidden;
}
.main-menu > li.menu-item-has-children a{
  padding:.75em .7em .7em 1.25em
}
.main-menu > li.menu-item-has-children:hover a{
  background-color:#373c59;
  color:#fff;
}
.main-menu > li.menu-item-has-children:after{
  content:'';
  position:absolute;
  right:.5em;
  top:1.2em;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 6px 5px 0 5px;
  border-color: #007bff transparent transparent
}
.main-menu > li.menu-item-has-children:hover,
.main-menu > li.menu-item-has-children:focus{
  overflow:visible;
  background-color:#373c59;
}
.main-menu ul.sub-menu{
  width:150px;
  position:absolute;
  /*top:100%;*/
  top:0;
  z-index:900;
  padding-top:3em;
}
.main-menu ul.sub-menu li{
  opacity:0
}
.main-menu > li.menu-item-has-children:hover ul.sub-menu,
.main-menu > li.menu-item-has-children:focus ul.sub-menu{
  top:100%;
  padding-top:0;
}
.main-menu > li.menu-item-has-children:hover ul.sub-menu li,
.main-menu > li.menu-item-has-children:focus ul.sub-menu li{
  opacity:1
}
.main-menu ul.sub-menu li{
  display:block
}
.main-menu ul.sub-menu a{
  display:block
}
.main-menu ul.sub-menu a:hover{
  background-color:#f15c4e;
}
a, .sub-menu, .menu-item{
  -webkit-transition: all .3s ease-out;
  -moz-transition: all .3s ease-out;
  -ms-transition: all .3s ease-out;
  -o-transition: all .3s ease-out;
  transition: all .3s ease-out;
}
</style>