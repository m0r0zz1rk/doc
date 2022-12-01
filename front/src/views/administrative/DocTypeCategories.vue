<template>
   <Header />
    <div id="main-content">
        <AdministrativeGrid>
            <div class="GridContent">
                <div v-if="seenContent">
                    <div style="position:relative;">
                        <div class="inl-blocks">
                            <a href="#" @click = "addSidebox();">
                                <div class="side-button-1-wr">
                                    <label class="side-button-1" for="side-checkbox">
                                        <div class="side-b side-open">
                                            Добавить <font-awesome-icon icon="fa-solid fa-plus" :style="{ color: '#fff' }"/>
                                        </div>
                                        <div class="side-b side-close">
                                            Закрыть
                                        </div>
                                    </label>
                                </div>
                            </a>
                        </div>&nbsp;
                        <div class="inl-blocks">
                            <a href="#" @click = "findSidebox();">
                                <div class="side-button-1-wr">
                                    <label class="side-button-1" for="side-checkbox">
                                        <div class="side-b side-open">
                                            Поиск <font-awesome-icon icon="fa-solid fa-magnifying-glass" :style="{ color: '#fff' }" />
                                        </div>
                                        <div class="side-b side-close">
                                            Закрыть
                                        </div>
                                    </label>
                                </div>
                            </a>
                        </div>
                    </div>
                    <table class="fl-table">
                        <thead>
                            <tr>
                                <th>Вид/тип документа <a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('type');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Наименование категории типа <a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('category');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Действия</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="category in listCategories">
                                <td style="text-align: left;">{{ category.type }}</td>
                                <td>{{ category.category }}</td>
                                <td class="action-td">
                                    <a href="javascript:void(0)" @click="editSidebox(category.id, category.type, category.category);">
                                        <font-awesome-icon icon="fa-solid fa-pen-to-square" :style="{ color: '#373c59' }"/>
                                    </a>&nbsp;&nbsp;
                                    <a href="javascript:void(0)" @click="deleteCategory(category.id);">
                                        <font-awesome-icon icon="fa-solid fa-trash" :style="{ color: '#373c59' }"/>
                                    </a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div v-if="seenLoad">
                    <img src="../../assets/gifs/load.gif" style="margin: 0 auto;">
                </div>
            </div>
        </AdministrativeGrid>
    </div>
    <SideBox>
        <template v-slot:side-chb>
            <input type="checkbox" id="side-checkbox" v-model="SideBoxChecked"/>
        </template>
        <template v-slot:sidebox-title>
            <p v-bind:class="[AddClass]">Новая категория типа документа</p>
            <p v-bind:class="[EditClass]">Изменение категории типа документа</p>
            <p v-bind:class="[FindClass]">Поиск по категориям типов документов</p>
        </template>
        <template v-slot:main-table-trs>
            <tr>
                <td>
                    <center>Вид документа: </center>
                </td>
                <td v-bind:class="[AddClass]">
                    <select ref="docKind" v-model="modelKind" class="form-control" @click="addOnChange();">
                        <option v-for="kind in listKinds">
                            {{ kind.kind }}
                        </option>
                    </select>
                </td>
                <td v-bind:class="[EditClass]">
                    <select ref="docKind" v-model="selectedKind" class="form-control" @click="editOnChange();">
                        <option v-for="kind in listKinds">
                            {{ kind.kind }}
                        </option>
                    </select>
                </td>
                <td v-bind:class="[FindClass]">
                    <input type="text" ref="FindKind" class="form-control text-center">
                </td>
            </tr>
            <tr>
                <td>
                    <center>Тип документа:</center>
                </td>
                <td v-bind:class="[AddClass]">
                    <select ref="docType" v-model="modelType" class="form-control">
                        <option v-for="type in availableTypes">
                            {{ type }}
                        </option>
                    </select>
                </td>
                <td v-bind:class="[EditClass]">
                    <select ref="docType" v-model="selectedType" class="form-control">
                        <option v-for="type in availableTypes">
                            {{ type }}
                        </option>
                    </select>
                </td>
                <td v-bind:class="[FindClass]">
                    <input type="text" ref="FindTypes" class="form-control text-center">
                </td>
            </tr>
            <tr>
                <td>
                    <center>Наименование категории типа:</center>
                </td>
                <td>
                    <input type="text" ref="DocCategory" class="form-control text-center">
                </td>
            </tr>
        </template>
        <template v-slot:sidebox-button>
            <div v-bind:class="[AddClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', AddClass]"
                    @click="addCategory();">Добавить</button>
            </div>
            <div v-bind:class="[EditClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', EditClass]"
                    @click="editCategory();">Изменить</button>
            </div>
            <div v-bind:class="[FindClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', FindClass]"
                    @click="findCategories();">Найти</button>
            </div>
        </template>
    </SideBox>
</template>

<script>
import AdministrativeGrid from '../../components/AdministrativeGrid.vue';
import SideBox from '../../components/sidebox_folder/SideBox.vue';
import Header from "../../components/Header.vue";
import LoadGif from "../../assets/gifs/load.gif";

export default {
    name: 'DocTypeCategories',
    data() {
      return {
        SideBoxChecked: false,
        seenLoad:true,
        seenContent:false,
        AddClass: 'sidebox-deactive',
        FindClass: 'sidebox-deactive',
        EditClass: 'sidebox-deactive',
        EditCatId: 0,
        selectKind: '',
        availableTypes: [],
        listKinds: [],
        listTypes: [],
        listCategories: [],
        buttonText: '',
        sort: 'type',
      }
    },
    components:
        {AdministrativeGrid, Header, SideBox},
    methods:{
        async loadKinds(){
            this.listKinds = await fetch(this.$store.state.backendUrl+'/api/docs/doc_kinds?ordering=kind', {
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
            this.listTypes = await fetch(this.$store.state.backendUrl+'/api/docs/doc_types?ordering=type', {
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
        async getCategories(find){
            let url = ''
            if (find){
                url = this.$store.state.backendUrl+'/api/docs/doc_categories?ordering='+this.sort+'&'+find
            } else {
                url = this.$store.state.backendUrl+'/api/docs/doc_categories?ordering='+this.sort
            }
            this.listCategories = await fetch(url, {
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
            this.seenLoad = false
            this.seenContent = true
        },
        sorted(obj){
            switch(obj){
                case "type":
                    if (this.sort == "type") {
                        this.sort = "-type"
                    } else {
                        this.sort = "type"
                    }
                    break;
                case "category":
                    if (this.sort == "category") {
                        this.sort = "-category"
                    } else {
                        this.sort = "category"
                    }
                    break;
                default:
                    break;
            }
            this.getCategories();
        },
        addSidebox(){
            this.AddClass = 'sidebox-active'
            this.EditClass = 'sidebox-deactive'
            this.FindClass = 'sidebox-deactive'
        },
        addOnChange(){
            let th = this
            this.availableTypes = []
            $.each(this.listTypes.filter(function (el){ return el.kind == th.modelKind}), function(index, el){
                th.availableTypes.push(el.type)
            })
        },
        editOnChange(){
            let th = this
            this.availableTypes = []
            $.each(this.listTypes.filter(function (el){ return el.kind == th.selectedKind}), function(index, el){
                th.availableTypes.push(el.type)
            })
        },
        async addCategory(){
            const add = await fetch(this.$store.state.backendUrl+'/api/docs/new_category/', {
              method: 'POST',
              headers: {
                'X-CSRFToken': getCookie("csrftoken"),
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token '+localStorage.getItem('access_token'),
              },
              body: JSON.stringify({
                'type': this.modelKind+' - '+this.modelType,
                'category': this.$refs.DocCategory.value
              })
            })
            .then(resp => resp.json())
            if (add.kind) {
                showBanner('.banner.error', add.kind)
                return false
            } else {
                this.SideBoxChecked = false;
                showBanner('.banner.success', add.success);
                this.getCategories();
            }
        },
        async editCategory() {
            if (confirm('Вы действительно хотите изменить категорию типа документа?')){
                const del = await fetch(this.$store.state.backendUrl+'/api/docs/edit_category/'+this.EditCatId, {
                  method: 'PATCH',
                  headers: {
                    'X-CSRFToken': getCookie("csrftoken"),
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Authorization': 'Token '+localStorage.getItem('access_token')
                  },
                  body: JSON.stringify({
                    'type': this.selectedKind+' - '+this.selectedType,
                    'category': this.$refs.DocCategory.value
                  })
                })
                .then(resp => resp.json())
                if (del.error){
                    showBanner('.banner.error', del.error)
                    return false
                } else {
                    showBanner('.banner.success', del.success);
                    this.getCategories();
                    this.SideBoxChecked = false
                }
                this.SideBoxChecked = false
            }
        },
        findSidebox(){
            this.AddClass = 'sidebox-deactive'
            this.EditClass = 'sidebox-deactive'
            this.FindClass = 'sidebox-active'
        },
        editSidebox(id, type, cat){
            this.EditCatId = id
            let arr = type.split(' - ')
            this.selectedKind = arr[0]
            this.editOnChange()
            this.selectedType = arr[1]
            this.$refs.DocCategory.value = cat
            this.AddClass = 'sidebox-deactive'
            this.EditClass = 'sidebox-active'
            this.FindClass = 'sidebox-deactive'
            this.SideBoxChecked = true
        },
        findCategories(){
            let find = ''
            if (this.$refs.FindKind.value != '') {
                find = 'kind='+this.$refs.FindKind.value+'&'
            }
            if (this.$refs.FindTypes.value != '') {
                find += 'type='+this.$refs.FindTypes.value+'&'
            }
             if (this.$refs.DocCategory.value != '') {
                find += 'category='+this.$refs.DocCategory.value
            }
            this.getCategories(find)
            $('#side-checkbox').prop('checked', false);
            showBanner('.banner.success', 'Поиск завершен');
        },
        async deleteCategory(id) {
            if (confirm('Вы действительно хотите удалить категорию типа документа?')){
                const del = await fetch(this.$store.state.backendUrl+'/api/docs/delete_category/'+id, {
                  method: 'delete',
                  headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Authorization': 'Token '+localStorage.getItem('access_token'),
                  }
                })
                .then(resp => resp.json())
                if (del.error){
                    showBanner('.banner.error', del.error)
                    return false
                } else {
                    showBanner('.banner.success', del.success);
                    this.getCategories();
                }
            }
        }
    },
    created(){
        this.loadKinds();
        this.loadTypes();
        this.getCategories();
    }
}
</script>

<style>
.table-content{
    display: none;
}
a{
  text-decoration: none;
}
.inl-blocks{
  display: inline-block;
  margin: 0 auto;
}
.copm-style{
  margin: 5px;
  width: 130px;
  text-decoration: none;
  position: relative;
  font-weight: bold;
  line-height: 20px;
  padding: 6px 15px;
  color: #FFF;
  background: #373c59;
  cursor: pointer;
  border-radius: 15px;
  display: block;
  margin: auto;
}
.text-center{
  text-align: center;
}
</style>