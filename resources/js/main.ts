import { createApp } from 'vue';
import AppList from './AppList.vue';
import AppForm from './AppForm.vue';

const appListMountPoint = document.getElementById("vueAppsList");
if(appListMountPoint){
    const appList = createApp(AppList)
    appList.mount(appListMountPoint);
}

const appFormMountPoint = document.getElementById("vueAppForm");
if(appFormMountPoint){
    const appForm = createApp(AppForm)
    appForm.mount(appFormMountPoint);
}