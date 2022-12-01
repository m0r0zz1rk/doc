<template>
   <Header />
    <div id="main-content">
        <AdministrativeGrid>
            <div class="GridContent">
                <div class="table-content">
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
                                <th>Наименование реквизита <a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('requisite');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Тэг (в шаблоне)<a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('tag');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Тип значений <a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('req_type');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Значения</th>
                                <th>Действия</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="requisite in listRequisites">
                                <td>{{ requisite.requisite }}</td>
                                <td>{{ requisite.tag }}</td>
                                <td>{{ requisite.req_type }}</td>
                                <td>
                                    <div v-if="arrTextPossible.includes(requisite.req_type)">
                                        -
                                    </div>
                                    <div v-if="requisite.req_type === 'Дата (краткий формат)'">
                                        ДД.ММ.ГГГГ г.
                                    </div>
                                    <div v-if="requisite.req_type === 'Дата (полный формат)'">
                                        ДД месяц ГГГГ г.
                                    </div>
                                    <div v-if="requisite.req_type === 'Выпадающий список'">
                                        <a href='javascript:void(0)' @click='showPossibleValues(requisite.id, requisite.requisite)'>
                                            <font-awesome-icon icon="fa-solid fa-list" :style="{ color: '#373c59' }"/>
                                        </a>
                                    </div>
                                </td>
                                <td class="action-td">
                                    <a href="javascript:void(0)" @click="editSidebox(requisite.id, requisite.req_type, requisite.requisite);">
                                        <font-awesome-icon icon="fa-solid fa-pen-to-square" :style="{ color: '#373c59' }"/>
                                    </a>&nbsp;&nbsp;
                                    <a href="javascript:void(0)" @click="deleteRequisite(requisite.id);">
                                        <font-awesome-icon icon="fa-solid fa-trash" :style="{ color: '#373c59' }"/>
                                    </a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="load">
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
            <p v-bind:class="[AddClass]">Новая реквизит</p>
            <p v-bind:class="[EditClass]">Изменение реквизита</p>
            <p v-bind:class="[FindClass]">Поиск по реквизитам</p>
        </template>
        <template v-slot:main-table-trs>
            <tr>
                <td>
                    <center>Наименование реквизита: </center>
                </td>
                <td v-bind:class="[AddClass]">
                    <input type="text" ref="addreq" class="form-control text-center">
                </td>
                <td v-bind:class="[EditClass]">
                    <input type="text" ref="editreq" class="form-control text-center">
                </td>
                <td v-bind:class="[FindClass]">
                    <input type="text" ref="findreq" class="form-control text-center">
                </td>
            </tr>
            <tr>
                <td>
                    <center>Тип значений реквизита:</center>
                </td>
                <td v-bind:class="[AddClass]">
                    <select v-model="addTypeReq" class="form-control">
                        <option v-for="type in listTypes">
                            {{ type.req_type }}
                        </option>
                    </select>
                </td>
                <td v-bind:class="[EditClass]">
                    <select v-model="editTypeReq" class="form-control">
                        <option v-for="type in listTypes">
                            {{ type.req_type }}
                        </option>
                    </select>
                </td>
                <td v-bind:class="[FindClass]">
                    <input type="text" ref="findreqtype" class="form-control text-center">
                </td>
            </tr>
        </template>
        <template v-slot:sidebox-button>
            <div v-bind:class="[AddClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', AddClass]"
                    @click="addRequisite();">Добавить</button>
            </div>
            <div v-bind:class="[EditClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', EditClass]"
                    @click="editRequisite();">Изменить</button>
            </div>
            <div v-bind:class="[FindClass]">
                <button type="button"
                    v-bind:class="['sidebox-add', 'copm-style', FindClass]"
                    @click="findRequisites();">Найти</button>
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
    name: 'DocRequisites',
    data() {
      return {
        SideBoxChecked: false,
        seenLoad:true,
        seenContent:false,
        AddClass: 'sidebox-deactive',
        FindClass: 'sidebox-deactive',
        EditClass: 'sidebox-deactive',
        editReqId: 0,
        listTypes: [],
        listRequisites: [],
        buttonText: '',
        sort: 'type',
        arrTextPossible: ['Текстовый', 'Числовой',],
        currentId: 0,
        currentReq: ''
      }
    },
    components:
        {AdministrativeGrid, Header, SideBox},
    methods:{
        async loadTypes(){
            this.listTypes = await fetch(this.$store.state.backendUrl+'/api/docs/requisite_types?ordering=req_type', {
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
        async getRequisites(find){
            let url = ''
            if (find){
                url = this.$store.state.backendUrl+'/api/docs/requisites?ordering='+this.sort+'&'+find
            } else {
                url = this.$store.state.backendUrl+'/api/docs/requisites?ordering='+this.sort
            }
            this.listRequisites = await fetch(url, {
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
            $('.load').empty();
            $('.table-content').css('display', 'block');
        },
        sorted(obj){
            switch(obj){
                case "requisite":
                    if (this.sort == "requisite") {
                        this.sort = "-requisite"
                    } else {
                        this.sort = "requisite"
                    }
                    break;
                case "tag":
                    if (this.sort == "tag") {
                        this.sort = "-tag"
                    } else {
                        this.sort = "tag"
                    }
                    break;
                case "req_type":
                    if (this.sort == "req_type") {
                        this.sort = "-req_type"
                    } else {
                        this.sort = "req_type"
                    }
                    break;
                default:
                    break;
            }
            this.getRequisites();
        },
        addSidebox(){
            this.AddClass = 'sidebox-active'
            this.EditClass = 'sidebox-deactive'
            this.FindClass = 'sidebox-deactive'
        },
        async addRequisite(){
            let add = await fetch(this.$store.state.backendUrl+'/api/docs/new_requisite/', {
              method: 'POST',
              headers: {
                'X-CSRFToken': getCookie("csrftoken"),
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token '+localStorage.getItem('access_token'),
              },
              body: JSON.stringify({
                'req_type': this.addTypeReq,
                'requisite': this.$refs.addreq.value
              })
            })
            .then(resp => resp.json())
            if (add.requisite) {
                showBanner('.banner.error', add.requisite)
                return false
            } else {
                this.SideBoxChecked = false
                showBanner('.banner.success', add.success);
                this.getRequisites();
            }
        },
        findSidebox(){
            this.AddClass = 'sidebox-deactive'
            this.EditClass = 'sidebox-deactive'
            this.FindClass = 'sidebox-active'
        },
        findRequisites(){
            let find = ''
            if (this.$refs.findreq.value != '') {
                find = 'requisite='+this.$refs.findreq.value+'&'
            }
            if (this.$refs.findreqtype.value != '') {
                find += 'type='+this.$refs.findreqtype.value
            }
            this.getRequisites(find)
            this.SideBoxChecked = false
            showBanner('.banner.success', 'Поиск завершен');
        },
        editSidebox(id, req_type, name){
            this.editTypeReq = req_type
            this.$refs.editreq.value = name
            this.editReqId = id
            this.AddClass = 'sidebox-deactive'
            this.EditClass = 'sidebox-active'
            this.FindClass = 'sidebox-deactive'
            this.SideBoxChecked = true
        },
        async editRequisite(){
            const ed = await fetch(this.$store.state.backendUrl+'/api/docs/requisite/'+this.editReqId+'/', {
              method: 'PATCH',
              headers: {
                'X-CSRFToken': getCookie("csrftoken"),
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token '+localStorage.getItem('access_token')
              },
              body: JSON.stringify({
                'req_type': this.editTypeReq,
                'requisite': this.$refs.editreq.value
              })
            })
            .then(resp => resp.json())
            if (ed.error){
                showBanner('.banner.error', ed.error)
                return false
            } else {
                showBanner('.banner.success', ed.success);
                this.SideBoxChecked = false
                this.getRequisites();
            }
        },
        async deleteRequisite(id) {
            if (confirm('Вы действительно хотите удалить реквизит?')){
                const del = await fetch(this.$store.state.backendUrl+'/api/docs/requisite/'+id+'/', {
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
                    this.getRequisites();
                }
            }
        },
        async addPossibleValue(){
            let add = await fetch(this.$store.state.backendUrl+'/api/docs/new_value/', {
                  method: 'POST',
                  headers: {
                    'X-CSRFToken': getCookie("csrftoken"),
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Authorization': 'Token '+localStorage.getItem('access_token'),
                  },
                  body: JSON.stringify({
                    'requisite': this.currentReq,
                    'possible_value': $('#NewPossVal').val()
                  })
                })
                .then(resp => {
                    if (resp.status == 200){
                        return resp.json()
                    } else {
                        showBanner('.banner.error', 'Произошла ошибка, повторите попытку позже')
                        return false
                    }
                })
                if (add.error || add.success) {
                    if (add.error) {
                        showBanner('.banner.error', add.error)
                        return false
                    } else {
                        $('#side-checkbox').prop('checked', false);
                        showBanner('.banner.success', add.success);
                        this.showPossibleValues(this.currentId, this.currentReq);
                    }
                }
        },
        async deleteCheckedValues(){
            if (confirm('Вы уверены, что хотите удалить выбранные элементы?')){
                $('.sidebox-adv-button').html('Удаление...');
                $('.sidebox-adv-button').prop('disabled', true);
                let arrValues = []
                let url = this.$store.state.backendUrl+'/api/docs/delete_value/'
                $('#PossValues:checked').each(async function() {
                    console.log(this.value)
                    await fetch(url+this.value, {
                      method: 'delete',
                      headers: {
                        'Content-Type': 'application/json;charset=UTF-8',
                        'Authorization': 'Token '+localStorage.getItem('access_token'),
                      }
                    })
                });

                this.showPossibleValues(this.currentId, this.currentReq)
            }
        },
        async showPossibleValues(id, name){
            $('#side-checkbox').prop('checked', true);
            this.currentId = id
            this.currentReq = name
            $('.side-title').html('Новое значение реквизита "'+name+'"');
            $('.side-advanced-title').html('Список существующих значений');
            $('.sidebox-table-trs').html('<tr><td ><img src="'+LoadGif+'" style="margin: 0 auto;"></td></tr>');
            let trs = `
                <tr>
                    <td>
                        <center>Значение: </center>
                    </td>
                    <td>
                        <input type="text" class="form-control text-center" id="NewPossVal">
                    </td>
                </tr>
            `
            $('.sidebox-button').html('Добавить');
            $('.sidebox-button').prop("onclick", null).off("click");
            $('.sidebox-button').click(this.addPossibleValue);
            $('.sidebox-table-trs').html(trs);
            let values = await fetch(this.$store.state.backendUrl+'/api/docs/req_values?req_name='+name, {
              method: 'GET',
              headers: {
                  'Authorization': 'Token '+localStorage.getItem('access_token'),
              },
            })
            .then(resp => resp.json())
            let adv_trs = ''
            $.each(values, function(index, value){
                 adv_trs += '<tr><td class="text-center">'+value.possible_value+'</td>'
                 adv_trs += `
                    <td class="text-center"><input type="checkbox" id="PossValues" value="`+value.id+`"></td>
                 `
            })
            $('.advanced-table-trs').html(adv_trs);
            $('.sidebox-adv-button').html('Удалить выбранные');
            $('.sidebox-adv-button').prop("onclick", null).off("click");
            $('.sidebox-adv-button').prop('disabled', false);
            $('.sidebox-adv-button').click(this.deleteCheckedValues);
            $('.advanced-sidebox').css('display', 'block')
        }
    },
    created(){
        this.getRequisites();
        this.loadTypes();
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