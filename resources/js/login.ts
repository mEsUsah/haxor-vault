import { createApp } from 'vue';
import Login from "./Login.vue"

// Login
const loginMountPoint = document.getElementById("vueUserLogin");
if(loginMountPoint){
    const appList = createApp(Login);
    appList.mount(loginMountPoint);
}