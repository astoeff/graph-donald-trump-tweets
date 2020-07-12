import Vue from 'vue';
import Router from 'vue-router';
import ByYear from './components/ByYear.vue';
import ByDay from './components/ByDay.vue';
import Russia from './components/Russia.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/by-year',
      name: 'By year',
      component: ByYear,
    },
    {
      path: '/by-day',
      name: 'By day',
      component: ByDay,
    },
    {
      path: '/russia',
      name: 'Russia',
      component: Russia,
    },
  ],
});
