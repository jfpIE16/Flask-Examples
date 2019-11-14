import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping';
import Books from './components/Books.vue'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/ping',
            name: 'Ping',
            component: Ping,
        },
        {
            path: '/books',
            name: 'Books',
            component: Books,
        },
    ],
    base: process.env.BASE_URL,
    mode: 'history',
});