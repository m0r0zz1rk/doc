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
                                    <a href="javascript:void(0)" @click="deleteCategory(category.id);">
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
    <SideBox />
</template>

<script>
import AdministrativeGrid from '../../components/AdministrativeGrid.vue';
import SideBox from '../../components/SideBox.vue';
import Header from "../../components/Header.vue";
import LoadGif from "../../assets/gifs/load.gif";

export default {
    name: 'DocTypeCategories',
    data() {
      return {
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
            $('.load').empty();
            $('.table-content').css('display', 'block');
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
            $('.side-title').html('Добавить новую категорию типа документа');
            $('.sidebox-table-trs').html('<tr><td ><img src="'+LoadGif+'" style="margin: 0 auto;"></td></tr>');
            let trs = `
                <tr>
                    <td>
                        <center>Вид документа: </center>
                    </td>
                    <td>
                        <select class="form-control" id="docKind">
            `
            $.each(this.listKinds, function(index, kind){
                trs += '<option>'+kind.kind+'</option>'
            })
            trs += `
                        </select>
                    </td>
                </tr>
                <tr>
                    <td>
                        <center>Тип документа:</center>
                    </td>
                    <td>
                        <select class="form-control" id="docType"></select>
                    </td>
                </tr>
                <tr>
                    <td>
                        <center>Наименование категории типа:</center>
                    </td>
                    <td>
                        <input type="text" class="form-control text-center" id="NewCategory">
                    </td>
                </tr>
            `
            $('.sidebox-button').html('Добавить');
            $('.sidebox-button').prop("onclick", null).off("click");
            $('.sidebox-button').click(this.addCategory);
            $('.sidebox-table-trs').html(trs);
            this.addOnchange()
            this.fillType()
        },
        addOnchange(){
            $('#docKind').prop("onchange", null).off("change");
            $('#docKind').change(this.fillType);
        },
        async fillType(){
            $("#docType").attr('disabled', true)
            $("#docType").find("option").remove()
            $.each(this.listTypes, function(index, tp){
                if (tp.kind == $('#docKind').val()) {
                    $('#docType').append('<option>'+tp.type+'</option>')
                }
            })
            $('#docType').attr('disabled', false)
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
                'type': $('#docKind').val()+' - '+$('#docType').val(),
                'category': $('#NewCategory').val()
              })
            })
            .then(resp => resp.json())
            if (add.kind) {
                showBanner('.banner.error', add.kind)
                return false
            } else {
                $('#side-checkbox').prop('checked', false);
                showBanner('.banner.success', add.success);
                this.getCategories();
            }
        },
        findSidebox(){
            $('.side-title').html('Поиск категории типа документа');
            $('.sidebox-table-trs').html('<tr><td ><img src="'+LoadGif+'" style="margin: 0 auto;"></td></tr>');
            let trs = `
                <tr>
                    <td>
                        <center>Вид документа:</center>
                    </td>
                    <td>
                        <input type="text" class="form-control text-center" id="FindKind">
                    </td>
                </tr>
                <tr>
                    <td>
                        <center>Тип документа:</center>
                    </td>
                    <td>
                        <input type="text" class="form-control text-center" id="FindType">
                    </td>
                </tr>
                <tr>
                    <td>
                        <center>Категория типа:</center>
                    </td>
                    <td>
                        <input type="text" class="form-control text-center" id="FindCategory">
                    </td>
                </tr>
            `
            $('.sidebox-button').html('Поиск');
            $('.sidebox-button').prop("onclick", null).off("click");
            $('.sidebox-button').click(this.findCategories);
            $('.sidebox-table-trs').html(trs);
        },
        findCategories(){
            let find = ''
            if ($('#FindKind').val() != '') {
                find = 'kind='+$('#FindKind').val()+'&'
            }
            if ($('#FindType').val() != '') {
                find += 'type='+$('#FindType').val()+'&'
            }
             if ($('#FindCategory').val() != '') {
                find += 'category='+$('#FindCategory').val()
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
        this.getCategories();
        this.loadKinds();
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