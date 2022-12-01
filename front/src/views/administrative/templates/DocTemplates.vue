<template>
   <Header />
    <div id="main-content">
        <AdministrativeGrid>
            <div class="GridContent">
                <div class="table-content">
                    <div style="position:relative;">
                        <div class="inl-blocks">
                            <router-link to="/administrative/guides/new_template">
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
                            </router-link>
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
                                <th>Вид,тип, категория документа<a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('category');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Дата создания <a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('date_create');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Имя шаблона <a href="javascript:void(0)"><div style="display: inline-block;" @click="sorted('name');">
                                    <font-awesome-icon icon="fa-solid fa-sort" />
                                </div></a></th>
                                <th>Реквизиты</th>
                                <th>Документ</th>
                                <th>Действия</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="template in listTemplates">
                                <td>{{ template.category }}</td>
                                <td>{{ template.date_create }}</td>
                                <td>{{ template.name }}</td>
                                <td>
                                    <a href='javascript:void(0)' @click='showRequisites(template.id, template.name)'>
                                        <i class='fa-solid fa-list' style='color: #373c59'></i>
                                    </a>
                                </td>
                                <td class="action-td">
                                    <a href="javascript:void(0)" @click="editTemplate(template.id);">
                                        <font-awesome-icon icon="fa-solid fa-pen-to-square" :style="{ color: '#373c59' }"/>
                                    </a>&nbsp;&nbsp;
                                    <a href="javascript:void(0)" @click="deleteTemplate(template.id);">
                                        <font-awesome-icon icon="fa-solid fa-trash" :style="{ color: '#373c59' }"/>
                                    </a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="load">
                    <img src="../../../assets/gifs/load.gif" style="margin: 0 auto;">
                </div>
            </div>
        </AdministrativeGrid>
    </div>
    <SideBox />
</template>

<script>
import AdministrativeGrid from '../../../components/AdministrativeGrid.vue';
import SideBox from '../../../components/sidebox_folder/SideBox.vue';
import Header from "../../../components/Header.vue";
import LoadGif from "../../../assets/gifs/load.gif";

export default {
    name: 'DocTemplates',
    data() {
      return {
        listTemplates: [],
        listRequisites: [],
        sortArr:['category', 'date_create', 'name'],
        sort: 'category',
        editElement: '',
        currentId: 0,
        currentReq: ''
      }
    },
    components:
        {AdministrativeGrid, Header, SideBox},
    methods:{
        async loadRequisites(){
            this.listRequisites = await fetch(this.$store.state.backendUrl+'/api/docs/requisites', {
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
        async getTemplates(find){
            let url = ''
            if (find){
                url = this.$store.state.backendUrl+'/api/docs/templates?ordering='+this.sort+'&'+find
            } else {
                url = this.$store.state.backendUrl+'/api/docs/templates?ordering='+this.sort
            }
            this.listTemplates = await fetch(url, {
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
            let sort_arr = this.sortArr
            let srt = this.sort
            $.each(sort_arr, function(index, st){
                if (obj == st){
                    if (srt == st) {
                        srt = "-"+st
                    } else {
                        srt = st
                    }
                }
            })
            this.sort = srt
            console.log(this.sort)
            /*this.getRequisites();*/
        },
        findSidebox(){
            $('.advanced-sidebox').css('display', 'none')
            $('.side-title').html('Поиск шаблонов');
            $('.sidebox-table-trs').html('<tr><td ><img src="'+LoadGif+'" style="margin: 0 auto;"></td></tr>');
            let trs = `
                <tr>
                    <td>
                        <center>Вид,тип, категория документа:</center>
                    </td>
                    <td>
                        <input type="text" class="form-control text-center" id="FindCategory">
                    </td>
                </tr>
                <tr>
                    <td>
                        <center>Дата создания:</center>
                    </td>
                    <td>
                        <input type="date" class="form-control text-center" id="FindDateCreate">
                    </td>
                </tr>
                <tr>
                    <td>
                        <center>Имя шаблона:</center>
                    </td>
                    <td>
                        <input type="text" class="form-control text-center" id="FindName">
                    </td>
                </tr>

            `
            $('.sidebox-button').html('Поиск');
            $('.sidebox-button').prop("onclick", null).off("click");
            $('.sidebox-button').click(this.findTemplates);
            $('.sidebox-table-trs').html(trs);
        },
        findTemplates(){
            let find = ''
            if ($('#FindReq').val() != '') {
                find = 'requisite='+$('#FindReq').val()+'&'
            }
            if ($('#FindType').val() != '') {
                find += 'type='+$('#FindType').val()
            }
            this.getRequisites(find)
            $('#side-checkbox').prop('checked', false);
            showBanner('.banner.success', 'Поиск завершен');
        },
        async editRequisite(id){
            this.editElement = id
            $('#side-checkbox').prop('checked', true);
            $('.advanced-sidebox').css('display', 'none')
            $('.side-title').html('Редактирование реквизита');
            $('.sidebox-table-trs').html('<tr><td ><img src="'+LoadGif+'" style="margin: 0 auto;"></td></tr>');
            let editRequisite = await fetch(this.$store.state.backendUrl+'/api/docs/requisite/'+id, {
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
            let trs = `
                <tr>
                    <td>
                        <center>Наименование:</center>
                    </td>
                    <td>
                        <input type="text" class="form-control text-center" id="EditReq"`
            trs += 'value="'+editRequisite.requisite +'"'
            trs += `>
                    </td>
                </tr>
                <tr>
                    <td>
                        <center>Тип значений:</center>
                    </td>
                    <td>
                        <select class="form-control text-center" id="reqType">
                            `
            $.each(this.listTypes, function(index, type){
                if (type.req_type == editRequisite.req_type) {
                    trs += '<option selected>'+type.req_type+'</option>'
                } else {
                    trs += '<option>'+type.req_type+'</option>'
                }
            })
            trs += `
                                        </select>
                    </td>
                </tr>
            `
            $('.sidebox-button').html('Изменить');
            $('.sidebox-button').prop("onclick", null).off("click");
            $('.sidebox-button').click(this.edit_req);
            $('.sidebox-table-trs').html(trs);
        },
        async edit_req(){
            const ed = await fetch(this.$store.state.backendUrl+'/api/docs/requisite/'+this.editElement+'/', {
              method: 'PATCH',
              headers: {
                'X-CSRFToken': getCookie("csrftoken"),
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token '+localStorage.getItem('access_token')
              },
              body: JSON.stringify({
                'req_type': $('#reqType').val(),
                'requisite': $('#EditReq').val()
              })
            })
            .then(resp => resp.json())
            if (ed.error){
                showBanner('.banner.error', ed.error)
                return false
            } else {
                showBanner('.banner.success', ed.success);
                $('#side-checkbox').prop('checked', false);
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
                 adv_trs += '<tr><td class="text-center">'+value. possible_value+'</td>'
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
        this.getTemplates();
        this.loadRequisites();
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