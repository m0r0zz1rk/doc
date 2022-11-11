<template>
    <div class="admin-grid">
        <div class="side-menu">
            <div class="wrapper">
            <div class="menu">
                <div class="d-flex flex-column flex-shrink-0 p-3" style="width: 280px;">
                    <a href="#"
                        class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none"
                        onclick="return false;">
                      <span style="font-weight: bold; margin: 0 auto;">Справочники</span>
                    </a><br>
                  <ul class="nav nav-pills flex-column mb-auto">
                      <li class="nav-item">
                        <a href="#" class="nav-link link-dark" id="DocKinds">
                            <router-link to="/administrative/guides/doc_kinds">
                                Виды документов
                            </router-link>
                        </a>
                      </li>
                      <li>
                        <a href="#" class="nav-link link-dark" id="DocTypes">
                            <router-link to="/administrative/guides/doc_types">
                                Типы документов
                            </router-link>
                        </a>
                      </li>
                      <li>
                        <a href="#" class="nav-link link-dark" id="DocTypeCategories">
                            <router-link to="/administrative/guides/doc_categories">
                                Категории типов документов
                            </router-link>
                        </a>
                      </li>
                      <li>
                        <a href="#" class="nav-link link-dark" id="DocRequisites">
                            <router-link to="/administrative/guides/doc_requisites">
                                Реквизиты документов
                            </router-link>
                        </a>
                      </li>
                      <li>
                        <a href="#" class="nav-link link-dark" id="DocTemplates">
                            <router-link to="/administrative/guides/doc_templates">
                                Шаблоны документов
                            </router-link>
                        </a>
                      </li>
                      <li>
                        <a href="#" class="nav-link link-dark">
                          Пусто
                        </a>
                      </li>
                    </ul>
              </div>
        </div>
    </div>
        </div>
        <div class="content">
            <slot></slot>
        </div>
    </div>
</template>

<script>
    import 'bootstrap/dist/js/bootstrap.min.js';
    export default {
        name: 'AdministrativeGrid',
        methods:{
           setActive(){
            $('#'+this.$route.name).addClass('link-active');
           }
        },
        mounted(){
          this.setActive()
        }
    }
</script>

<style>
  .admin-grid{
    margin: 0 auto;
    width: 90vw;
    height: 75vh;
    display: grid;
    column-gap: 100px;
    grid-template-columns: 15vw 70vw;

  }
  .side-menu{
     height: 80%;
     justify-self: center;
     align-self: center;
  }
  .content{
     height: 80%;
     justify-self: center;
     align-self: center;
  }
  .menu{
    background-color: #373c59;
  }
  a{
    color:#fff;
    text-decoration: none;
  }
  a:hover{
     color:#fff;
  }
  .link-active{
    background-color: #f15c4e;
  }

</style>