
import { createApp } from 'vue';
import { VueReCaptcha} from 'vue-recaptcha-v3'
import Login from "./Login.vue"
import Register from "./Register.vue"

const captchaSiteKey = document.querySelector('meta[name="captcha-site-key"]')?.getAttribute('content');

// Login
const loginMountPoint = document.getElementById("vueUserLogin");
if(loginMountPoint){
    const userLogin = createApp(Login);
    userLogin.use(VueReCaptcha, { 
        siteKey: captchaSiteKey??'',
    });
    userLogin.mount(loginMountPoint);
}

// Register
const registerMountPoint = document.getElementById("vueUserRegister");
if(registerMountPoint){
    const userRegister = createApp(Register);
    userRegister.use(VueReCaptcha, { 
        siteKey: captchaSiteKey??'',
    });
    userRegister.mount(registerMountPoint);
}