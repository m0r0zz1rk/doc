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
            <div id="category-content">
                <table class="fl-table cat-table">
                    <thead>
                        <tr>
                            <td width="40%">Вид документа</td>
                            <td width="30%">Тип документа</td>
                            <td width="30%">Категория документа</td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <select class="form-control" id="ChooseKind" @change="changeDocKind($event)">
                                    <option v-for="kind in listKinds">
                                        {{ kind.kind }}
                                    </option>
                                </select>
                            </td>
                            <td>
                                <select class="form-control" id="ChooseType" @change="changeDocType($event)" :disabled="disabledTypes">
                                    <option v-for="type in selectedTypes">
                                        {{ type }}
                                    </option>
                                </select>
                            </td>
                            <td>
                                <select class="form-control" id="ChooseCategory" :disabled="disabledCategories">
                                    <option v-for="category in selectedCategories">
                                        {{ category }}
                                    </option>
                                </select>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div id="category-load">
                <img src="../../../assets/gifs/load.gif" style="margin: 0 auto;">
            </div>
        </template>
        <template v-slot:info-ch>
            <table class="fl-table cat-table">
                <tr>
                    <td>Дата создания шаблона</td>
                    <td><input type="date" class="form-control text-center" v-model="currentDate" disabled></td>
                </tr>
                <tr></tr>
                <tr>
                    <td>Наименование шаблона</td>
                    <td><textarea class="form-control" id="TemplateName"></textarea></td>
                </tr>
            </table>
        </template>
        <template v-slot:reqs-ch>
            <a href="#" @click="addSidebox();">
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
            <table class="fl-table cat-table">
                <thead>
                    <th>Наименование реквизита</th>
                    <th>Тип значений</th>
                    <th>Значения</th>
                    <th>Убрать из шаблона</th>
                </thead>
                <tbody>
                    <tr v-for="requisite in selectedRequisites">
                        <td>{{ requisite.requisite }}</td>
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
                                <a href='javascript:void(0)' @click=''>
                                    <font-awesome-icon icon="fa-solid fa-list" :style="{ color: '#373c59' }"/>
                                </a>
                            </div>
                        </td>
                        <td>
                            <a href="javascript:void(0)" @click="">
                                <font-awesome-icon icon="fa-solid fa-trash" :style="{ color: '#373c59' }"/>
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </template>
    </DocGrid>
    <SideBox />
</template>

<script>
import DocGrid from '../../../components/DocGrid.vue';
import SideBox from '../../../components/sidebox_folder/SideBox.vue';
import Header from "../../../components/Header.vue";
import LoadGif from "../../../assets/gifs/load.gif";

export default {
    name: 'NewTemplate',
    data() {
      return {
        arrTextPossible: ['Текстовый', 'Числовой',],
        listKinds: [],
        listTypes: [],
        selectedTypes: [],
        disabledTypes: true,
        listCategories: [],
        selectedCategories: [],
        disabledCategories: true,
        listRequisites: [],
        selectedRequisites: [],
        currentDate: new Date().toISOString().substr(0, 10)
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
            $('#category-content').css('display', 'block')
            $('#category-load').css('display', 'none')
        },
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
            $('#category-content').css('display', 'block')
            $('#category-load').css('display', 'none')
            console.log(this.listRequisites)
        },
        showCategoryContent(){
            $('#category-content').css('display', 'block')
            $('#category-load').css('display', 'none')
        },
        hideCategoryContent(){
            $('#category-content').css('display', 'none')
            $('#category-load').css('display', 'block')
        },
        changeDocKind(event){
            this.hideCategoryContent()
            let lTypes = ['Выберите из списка']
            $.each(this.listTypes, function(index, type){
                if (event.target.value == type.kind){
                    lTypes.push(type.type)
                }
            })
            this.selectedTypes = lTypes
            this.disabledTypes = false
            this.selectedCategories = []
            this.disabledCategories = true
            this.showCategoryContent()
        },
        changeDocType(event){
            this.hideCategoryContent()
            let lCategories = []
            let t = document.getElementById('ChooseKind').value+' - '+document.getElementById('ChooseType').value
            $.each(this.listCategories, function(index, cat){
                if (cat.type == t){
                    lCategories.push(cat.category)
                }
            })
            this.selectedCategories = lCategories
            this.disabledCategories = false
            this.showCategoryContent()
        },
        addSidebox(){
            $('.advanced-sidebox').css('display', 'none');
            $('.sidebox-button').css('display', 'none');
            $('.sidebox-button').prop('disabled', true);
            $('.side-title').html('Добавить реквизит к шаблону');
            $('.sidebox-table-trs').html('<tr><td ><img src="'+LoadGif+'" style="margin: 0 auto;"></td></tr>');
            let th = this
            let reqs = this.listRequisites
            let trs = ''
            $.each(reqs, async function(index, r){
                let vals = ''
                trs += '<tr class="border_bottom"><td class="text-center"><b>'+r.requisite+'</b></td><td class="text-center">'
                if (th.tdValueReqType(r.req_type) != 'list') {
                    trs += th.tdValueReqType(r.req_type)
                } else {
                    trs += '<button type="button" id="showPossVal" name="'+r.requisite+'" class="copm-style">Просмотр значений</button>'
                }
                trs += `
                        </td>
                    </tr>
                `
                console.log(trs)
            })
            $('.sidebox-button').html('Добавить');
            $('.sidebox-button').prop("onclick", null).off("click");
            $('.sidebox-button').click(this.addRequisite);
            $('.sidebox-table-trs').html(trs);

        },
        tdValueReqType(text, name){
            if (this.arrTextPossible.includes(text)){
                if (text == 'Текстовый') {
                    return 'Текстовое значение'
                } else {
                    return 'Числовое значение'
                }
            } else {
                if (text == 'Дата (краткий формат)') {
                    return 'ДД.ММ.ГГГГ г.'
                } else if (text == 'Дата (полный формат)') {
                    return 'ДД месяц ГГГГ г.'
                } else {
                    return 'list'
                }
            }
        },
        async showPossibleValuesReq(name){
            $('.side-advanced-title').html('Список возможных значений реквизита "'+name+'"')
            let adv_trs = ''
            let values = await fetch(th.$store.state.backendUrl+'/api/docs/req_values?req_name='+name, {
              method: 'GET',
              headers: {
                  'Authorization': 'Token '+localStorage.getItem('access_token'),
              },
            })
            .then(resp => resp.json())
            .then(values => {
                $.each(values, function (i, val){
                    adv_trs += val.possible_value+'<br>'
                })
            })
            $('.advanced-table-trs').html(adv_trs)
            $('.advanced-sidebox').css('display', 'block')
        },
        getTypes(){

        }
    },
    created(){
        this.loadKinds();
        this.loadTypes();
        this.loadCategories();
        this.loadRequisites();
        this.showCategoryContent();
    }
}
</script>

<style>
#TemplateName{
  resize: both;
  width: 100%;
}
#category-content, #info-content,
#reqs-content, #doc-content{
    display: none
}
.cat-table {
    width: 50%;
}
</style>