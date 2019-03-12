import Vue from 'vue';
import VueFire from 'vuefire';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;
import firebase from 'firebase/app'
import 'firebase/firestore'
Vue.use(VueFire)
let config = {
  apiKey: "AIzaSyBsQwYsREGENu4ce46s1ImytA0aj7S-1HQ",
  authDomain: "clubtain.firebaseapp.com",
  databaseURL: "https://clubtain.firebaseio.com",
  projectId: "clubtain",
  storageBucket: "clubtain.appspot.com",
  messagingSenderId: "883363420961"
};
firebase.initializeApp(config)
export const db = firebase.firestore()

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
