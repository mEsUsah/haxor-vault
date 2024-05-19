import { createApp } from 'vue';
import AppList from './AppList.vue';
import AppCreate from './AppCreate.vue';
import AppDetails from './AppDetails.vue';
import CredentialCreate from './CredentialCreate.vue';
import CredentialDetails from './CredentialDetails.vue';

// Dashboard
const appListMountPoint = document.getElementById("vueAppsList");
if(appListMountPoint){
    const appList = createApp(AppList);
    appList.mount(appListMountPoint);
}

// Apps
const appCreateMountPoint = document.getElementById("vueAppCreate");
if(appCreateMountPoint){
    const appForm = createApp(AppCreate);
    appForm.mount(appCreateMountPoint);
}

const appDetailsMountPoint = document.getElementById("vueAppDetails");
if(appDetailsMountPoint){
    const appDetails = createApp(AppDetails);
    appDetails.mount(appDetailsMountPoint);
}

// Credentials
const credentialCreateMountPoint = document.getElementById("vueCredentialCreate");
if(credentialCreateMountPoint){
    const credentialForm = createApp(CredentialCreate);
    credentialForm.mount(credentialCreateMountPoint);
}

const credentialDetailMountPoint = document.getElementById("vueCredentialDetails");
if(credentialDetailMountPoint){
    const credentialDetails = createApp(CredentialDetails);
    credentialDetails.mount(credentialDetailMountPoint);
}