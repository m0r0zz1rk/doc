<template>
    <Header />
    <router-link to="/administrative/guides/doc_templates">
        <div class="side-button-1-wr">
            <label class="side-button-1" for="side-checkbox">
                <div class="side-b side-open">
                   <font-awesome-icon icon="fa-solid fa-arrow-left" :style="{ color: '#fff' }"/> Назад
                </div>
                <div class="side-b side-close">
                    Закрыть
                </div>
            </label>
        </div>
    </router-link>
    <h4><center>Новый шаблон</center></h4>
    <DocGrid>
        <template v-slot:cat-ch>
            <table class="fl-table cat-table">
                <thead>
                    <tr>
                        <td>Вид документа</td>
                        <td>Тип документа</td>
                        <td>Категория документа</td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            <select class="form-control" @change="getTypes()">
                                <option v-for="kind in listKinds">
                                    {{ kind.kind }}
                                </option>
                            </select>
                        </td>
                        <td>
                            <select class="form-control" id="ChooseType">
                            </select>
                        </td>
                        <td>
                            <select class="form-control" id="ChooseCategory">
                            </select>
                        </td>
                    </tr>
                </tbody>
            </table>
        </template>
    </DocGrid>
</template>

<script>
import DocGrid from '../../../components/DocGrid.vue';
import SideBox from '../../../components/SideBox.vue';
import Header from "../../../components/Header.vue";

export default {
    name: 'NewTemplate',
    data() {
      return {
        listKinds: [],
        listTypes: [],
        listCategories: [],
        listRequisites: [],
        sortArr:['category', 'date_create', 'name'],
        sort: 'category',
        editElement: '',
        currentId: 0,
        currentReq: ''
      }
    },
    components:
        {DocGrid, Header, SideBox},
    methods: {
        async loadKinds(){
            this.listKinds = await fetch(this.$store.state.backendUrl+'/api/docs/doc_kinds', {
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
        },
        async loadTypes(){
            this.listTypes = await fetch(this.$store.state.backendUrl+'/api/docs/doc_types', {
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
        },
        async loadCategories(){
            this.listCategories = await fetch(this.$store.state.backendUrl+'/api/docs/doc_categories', {
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
        },
        getTypes(){
            console.log(this.listTypes);
            console.log(this.listCategories);
        }
    },
    created(){
        this.loadKinds();
        this.loadTypes();
        this.loadCategories();
    }
}
</script>

<style>
.cat-table {
    width: 50%;
}
</style>