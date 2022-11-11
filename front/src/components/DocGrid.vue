<template>
    <div class="doc-grid">
        <div class="grid-row category-chapter">
            <b><center>Вид, тип, категория документа</center></b>
            <div>
                <slot name="cat-ch"></slot>
            </div>
        </div>
        <div class="grid-row info-chapter">
            <b><center>Информация о шаблоне</center></b>
            <div>
                <slot name="info-ch"></slot>
            </div>
        </div>
        <div class="grid-row reqs-chapter">
            <b><center>Реквизиты шаблона</center></b>
            <div>
                <slot name="reqs-ch"></slot>
            </div>
        </div>
        <div class="grid-row doc-chapter">
            <b><center>Документ шаблона</center></b>
            <div>
                <slot name="doc-ch"></slot>
            </div>
        </div>
    </div>
</template>

<script>
    import 'bootstrap/dist/js/bootstrap.min.js';
    export default {
        name: 'DocGrid',
        methods:{

        }
    }
</script>

<style>
  .doc-grid{
    margin: 0 auto;
    width: 90vw;
    display: grid;
    row-gap: 25px;
    grid-template-rows: auto auto auto auto;
    justify-items: stretch;
  }
  .grid-row{
     border-radius: 15px;
     border: 2px solid #373c59;
     color: black;
  }
</style>