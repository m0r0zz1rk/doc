import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import 'jquery/src/jquery.js';
import 'popper.js/dist/popper.js';
import 'bootstrap/dist/js/bootstrap.min.js';
import '../src/assets/css/fonts.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {  faUser,
          faSliders,
          faRightFromBracket,
          faSort,
          faTrash,
          faPlus,
          faMagnifyingGlass,
          faPenToSquare,
          faList,
          faArrowLeft} from '@fortawesome/free-solid-svg-icons'

library.add(faUser,
            faSliders,
            faRightFromBracket,
            faSort,
            faTrash,
            faPlus,
            faMagnifyingGlass,
            faPenToSquare,
            faList,
            faArrowLeft)

createApp(App).use(router).use(store).component('font-awesome-icon', FontAwesomeIcon).mount('#app')

