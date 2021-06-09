import { createApp } from 'vue'
import { createWebHistory , createRouter } from "vue-router";
import Toast, { TYPE } from "vue-toastification";
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
import IconComponent from './components/IconComponent.vue'


const options = {
  toastDefaults: {
      // ToastOptions object for each type of toast
      [TYPE.ERROR]: {
          timeout: 10000,
          closeButton: false,
      },
      [TYPE.SUCCESS]: {
          icon:  IconComponent,
          closeButtonClassName: "toast-button-class",
          toastClassName: "toast-custom-background",
          bodyClassName: ["toast-black-font-stlye"]
      }    
  }
};


const routes = [
    {
      path: '/',
      name: 'Home',
      component: Home,
      props: true
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
      path: '/login/:uid/:token',
      name: 'Activate',
      component: Login,
      props: true
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

createApp(App).use(store).use(router).use(Toast, options).mount('#app')

