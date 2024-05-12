import { createApp } from 'vue';
import AppList from './AppList.vue';
import AppDetails from './AppDetails.vue';
import CreateApp from './AppCreate.vue';
import CreateCredential from './CredentialCreate.vue';

// Dashboard
const appListMountPoint = document.getElementById("vueAppsList");
if(appListMountPoint){
    const appList = createApp(AppList);
    appList.mount(appListMountPoint);
}

// Apps
const appCreateMountPoint = document.getElementById("vueAppCreate");
if(appCreateMountPoint){
    const appForm = createApp(CreateApp);
    appForm.mount(appCreateMountPoint);
}

const appDetailsMountPoint = document.getElementById("vueAppDetails");
if(appDetailsMountPoint){
    const appForm = createApp(AppDetails);
    appForm.mount(appDetailsMountPoint);
}

// Credentials
const credentialCreateMountPoint = document.getElementById("vueCredentialCreate");
if(credentialCreateMountPoint){
    const credentialForm = createApp(CreateCredential);
    credentialForm.mount(credentialCreateMountPoint);
}