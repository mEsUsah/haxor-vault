import { createApp } from 'vue';
import Login from "./Login.vue"
import Register from "./Register.vue"

// Login
const loginMountPoint = document.getElementById("vueUserLogin");
if(loginMountPoint){
    const appList = createApp(Login);
    appList.mount(loginMountPoint);
}

// Register
const registerMountPoint = document.getElementById("vueUserRegister");
if(registerMountPoint){
    const appList = createApp(Register);
    appList.mount(registerMountPoint);
}