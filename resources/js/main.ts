import { createApp } from 'vue';
import AppList from './AppList.vue';
import CreateApp from './CreateApp.vue';

const appListMountPoint = document.getElementById("vueAppsList");
if(appListMountPoint){
    const appList = createApp(AppList)
    appList.mount(appListMountPoint);
}

const appCreateMountPoint = document.getElementById("vueAppForm");
if(appCreateMountPoint){
    const appForm = createApp(CreateApp)
    appForm.mount(appCreateMountPoint);
}