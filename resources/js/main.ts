import { createApp } from 'vue';
import AppList from './AppList.vue';

const appListMountPoint = document.getElementById("vueAppsList");
if(appListMountPoint){
    const appList = createApp(AppList)
    appList.mount(appListMountPoint);
}
