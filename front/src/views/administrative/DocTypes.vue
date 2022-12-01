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
                                <th>Наименование вида документа <a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('kind');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Наименование типа документа <a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('type');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Действия</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="type in listTypes">
                                <td>{{ type.kind }}</td>
                                <td>{{ type.type }}</td>
                                <td>
                                    <a href="javascript:void(0)" @click="editSidebox(type.id, type.kind, type.type);">
                                        <font-awesome-icon icon="fa-solid fa-pen-to-square" :style="{ color: '#373c59' }"/>
                                    </a>&nbsp;&nbsp;
                                    <a href="javascript:void(0)" @click="deleteType(type.id);">
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
            <p v-bind:class="[AddClass]">Новый тип документа</p>
            <p v-bind:class="[EditClass]">Изменение типа документа</p>
            <p v-bind:class="[FindClass]">Поиск по типам документов</p>
        </template>
        <template v-slot:main-table-trs>
            <tr>
                <td>
                    <center>Вид документа: </center>
                </td>
                <td v-bind:class="[AddClass]">
                    <select ref="docKind" v-model="newtypekind" class="form-control">
                        <option v-for="kind in listKinds">
                            {{ kind.kind }}
                        </option>
                    </select>
                </td>
                <td v-bind:class="[EditClass]">
                    <select ref="docKind" v-model="selectedKind" class="form-control">
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
                    <center>Наименование типа документа:</center>
                </td>
                <td>
                    <input type="text" ref="DocType" class="form-control text-center">
                </td>
            </tr>
        </template>
        <template v-slot:sidebox-button>
            <div v-bind:class="[AddClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', AddClass]"
                    @click="addType();">Добавить</button>
            </div>
            <div v-bind:class="[EditClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', EditClass]"
                    @click="editType();">Изменить</button>
            </div>
            <div v-bind:class="[FindClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', FindClass]"
                    @click="findTypes();">Найти</button>
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
    name: 'DocTypes',
    data() {
      return {
        SideBoxChecked: false,
        seenLoad:true,
        seenContent:false,
        AddClass: 'sidebox-deactive',
        FindClass: 'sidebox-deactive',
        EditClass: 'sidebox-deactive',
        EditTypeId: 0,
        listKinds: [],
        listTypes: [],
        buttonText: '',
        sort: 'kind'
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
            console.log(this.listKinds)
        },
        async getTypes(find){
            let url = ''
            if (find){
                url = this.$store.state.backendUrl+'/api/docs/doc_types?ordering='+this.sort+'&'+find
            } else {
                url = this.$store.state.backendUrl+'/api/docs/doc_types?ordering='+this.sort
            }
            this.listTypes = await fetch(url, {
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
                case "kind":
                    if (this.sort == "kind") {
                        this.sort = "-kind"
                    } else {
                        this.sort = "kind"
                    }
                    break;
                case "type":
                    if (this.sort == "type") {
                        this.sort = "-type"
                    } else {
                        this.sort = "type"
                    }
                    break;
                default:
                    break;
            }
            this.getTypes();
        },
        findTypes(){
            let find = ''
            if (this.$refs.FindKind.value != '') {
                find = 'kind='+this.$refs.FindKind.value
            }
            if (this.$refs.DocType.value != '') {
                find += 'type='+this.$refs.DocType.value
            }
            this.getTypes(find)
            this.SideBoxChecked = false
            showBanner('.banner.success', 'Поиск завершен')
        },
        addSidebox(){
            this.AddClass = 'sidebox-active'
            this.EditClass = 'sidebox-deactive'
            this.FindClass = 'sidebox-deactive'
        },
        findSidebox(){
            this.AddClass = 'sidebox-deactive'
            this.EditClass = 'sidebox-deactive'
            this.FindClass = 'sidebox-active'
        },
        editSidebox(id, kind, type){
            this.EditTypeId = id
            this.selectedKind = kind
            this.$refs.DocType.value = type
            this.AddClass = 'sidebox-deactive'
            this.EditClass = 'sidebox-active'
            this.FindClass = 'sidebox-deactive'
            this.SideBoxChecked = true
        },
        async addType(){
            const add = await fetch(this.$store.state.backendUrl+'/api/docs/new_type/', {
              method: 'POST',
              headers: {
                'X-CSRFToken': getCookie("csrftoken"),
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token '+localStorage.getItem('access_token'),
              },
              body: JSON.stringify({
                'kind': this.newtypekind,
                'type': this.$refs.DocType.value
              })
            })
            .then(resp => resp.json())
            if (add.kind) {
                showBanner('.banner.error', add.kind)
                return false
            } else {
                this.SideBoxChecked = false
                showBanner('.banner.success', add.success);
                this.getTypes();
            }
        },
        async editType() {
            if (confirm('Вы действительно хотите изменить тип документа?')){
                const del = await fetch(this.$store.state.backendUrl+'/api/docs/edit_type/'+this.EditTypeId, {
                  method: 'PATCH',
                  headers: {
                    'X-CSRFToken': getCookie("csrftoken"),
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Authorization': 'Token '+localStorage.getItem('access_token')
                  },
                  body: JSON.stringify({
                    'kind': this.selectedKind,
                    'type': this.$refs.DocType.value
                  })
                })
                .then(resp => resp.json())
                if (del.error){
                    showBanner('.banner.error', del.error)
                    return false
                } else {
                    showBanner('.banner.success', del.success);
                    this.getTypes();
                }
                this.SideBoxChecked = false
            }
        },
        async deleteType(id) {
            if (confirm('Вы действительно хотите удалить тип документа?')){
                const del = await fetch(this.$store.state.backendUrl+'/api/docs/delete_type/'+id, {
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
                    this.getTypes();
                }
            }
        }
    },
    created(){
        this.getTypes();
        this.loadKinds();
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