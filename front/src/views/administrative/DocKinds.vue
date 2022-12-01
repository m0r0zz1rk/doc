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
                                <th>Наименование <a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted();">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Действия</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="kind in listKinds">
                                <td>{{ kind.kind }}</td>
                                <td>
                                    <a href="javascript:void(0)" @click="editSidebox(kind.id, kind.kind);">
                                        <font-awesome-icon icon="fa-solid fa-pen-to-square" :style="{ color: '#373c59' }"/>
                                    </a>&nbsp;&nbsp;
                                    <a href="javascript:void(0)" @click="deleteKind(kind.id);">
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
            <input type="checkbox" id="side-checkbox" v-model="SideBoxchecked"/>
        </template>
        <template v-slot:sidebox-title>
            <p v-bind:class="[AddClass]">Новый вид документа</p>
            <p v-bind:class="[EditClass]">Изменение вида документа</p>
            <p v-bind:class="[FindClass]">Поиск по видам документа</p>
        </template>
        <template v-slot:main-table-trs>
            <tr>
                <td>
                    <center>Наименование:</center>
                </td>
                <td>
                    <input ref="kind" type="text" class="form-control text-center">
                </td>
            </tr>
        </template>
        <template v-slot:sidebox-button>
            <div v-bind:class="[AddClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', AddClass]"
                    @click="addKind();">Добавить</button>
            </div>
            <div v-bind:class="[EditClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', EditClass]"
                    @click="editKind();">Изменить</button>
            </div>
            <div v-bind:class="[FindClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', FindClass]"
                    @click="findKinds();">Найти</button>
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
    name: 'DocKinds',
    data() {
      return {
        seenLoad: true,
        seenContent: false,
        SideBoxchecked: false,
        AddClass: 'sidebox-deactive',
        FindClass: 'sidebox-deactive',
        EditClass: 'sidebox-deactive',
        EditKindId: 0,
        listKinds: [],
        trs: '',
        buttonText: '',
        sort: 'kind'
      }
    },
    components:
        {AdministrativeGrid, Header, SideBox},
    methods:{
        async getKinds(find){
            let url = ''
            if (find){
                url = this.$store.state.backendUrl+'/api/docs/doc_kinds?ordering='+this.sort+'&kind='+find
            } else {
                url = this.$store.state.backendUrl+'/api/docs/doc_kinds?ordering='+this.sort
            }
            this.listKinds = await fetch(url, {
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
            this.seenContent = true
            this.seenLoad = false

        },
        sorted(){
            if (this.sort == 'kind') {
                this.sort='-kind';
            } else {
                this.sort='kind';
            }
            this.getKinds();
        },
        findKinds(){
            this.getKinds(this.$refs.kind.value)
            this.SideBoxchecked = false
            showBanner('.banner.success', 'Поиск завершен');
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
        editSidebox(id, name){
            this.EditKindId = id
            this.SideBoxchecked = true,
            this.$refs.kind.value = name
            this.AddClass = 'sidebox-deactive'
            this.EditClass = 'sidebox-active'
            this.FindClass = 'sidebox-deactive'
        },
        async addKind(){
            const add = await fetch(this.$store.state.backendUrl+'/api/docs/new_kind/', {
              method: 'POST',
              headers: {
                'X-CSRFToken': getCookie("csrftoken"),
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token '+localStorage.getItem('access_token'),
              },
              body: JSON.stringify({
                'kind': this.$refs.kind.value
              })
            })
            .then(resp => resp.json())
            if (add.kind) {
                showBanner('.banner.error', add.kind)
                return false
            } else {
                $('#side-checkbox').prop('checked', false);
                showBanner('.banner.success', add.success);
                this.getKinds();
            }
        },
        async editKind() {
            if (confirm('Вы действительно хотите изменить вид документа?')){
                const del = await fetch(this.$store.state.backendUrl+'/api/docs/edit_kind/'+this.EditKindId, {
                  method: 'PATCH',
                  headers: {
                    'X-CSRFToken': getCookie("csrftoken"),
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Authorization': 'Token '+localStorage.getItem('access_token')
                  },
                  body: JSON.stringify({
                    'kind': this.$refs.kind.value,
                  })
                })
                .then(resp => resp.json())
                if (del.error){
                    showBanner('.banner.error', del.error)
                    return false
                } else {
                    showBanner('.banner.success', del.success);
                    this.getKinds();
                }
                this.SideBoxchecked = false
            }
        },
        async deleteKind(id) {
            if (confirm('Вы действительно хотите удалить вид документа?')){
                const del = await fetch(this.$store.state.backendUrl+'/api/docs/delete_kind/'+id, {
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
                    this.getKinds();
                }
            }
        }
    },
    created(){
        this.getKinds();
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