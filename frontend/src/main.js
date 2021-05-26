import { createApp } from 'vue'
import { createWebHistory , createRouter } from "vue-router";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import Home from './views/Home.vue'
import Register from './views/Register.vue'
import Login from './views/Login.vue'
import ResetPassword from './views/ResetPassword.vue'
import ChangePassword from './views/ChangePassword.vue'
import MotionView from './views/MotionView.vue'
import MotionSuggest from './views/MotionSuggest.vue'
import store from './store/store'
import Profile from './views/Profile.vue'
import App from './App.vue'

const routes = [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/reset',
      name: 'ResetPassword',
      component: ResetPassword
    },
    {
      path: '/change/:uid/:token',
      name: 'ChangePassword',
      component: ChangePassword
    },
    {
      path: '/motion/:id',
      name: 'MotionView',
      component: MotionView,
      props: true
    },
    {
      path: '/motionSuggest',
      name: 'MotionSuggest',
      component: MotionSuggest
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    }
  ];

const router = createRouter({
  history: createWebHistory(),
  routes,
})

createApp(App).use(store).use(router).use(Toast, {}).mount('#app')

