<template>
    <form class="form__wrapper">
        <div class="form__field">
            <select name="apptype" v-model="app.apptype">
                <option value="" disabled>Select type:</option>
                <option v-for="appType in appTypes" :value="appType.id">
                    {{ appType.name }}
                </option>
            </select>
        </div>
        <div class="form__field">
            <input v-model="app.name" type="text" name="name" placeholder="Name" maxlength="100">
        </div>
        <div class="form__buttons">
            <button 
                :disabled="disableSubmit"
                @click="saveApp"
                type="submit" class="button">Save</button>
            <a href="/dashboard" class="button button--nautral">Back</a>
            <a class="button button--danger"
                v-if="!newApp"
                @click="destroyApp"
            >Delete</a>
        </div>
    </form>
</template>

<script lang="ts">
import { defineComponent, PropType, onMounted, ref, reactive, computed, watch } from 'vue';
import { AppType, App, AppSchema } from '../components/interfaces.ts';
import { validateAppSchema } from '../components/validateAppSchema.ts';
const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

export default defineComponent({
    props: {
        appTypes: {
            type: Array as PropType<AppType[]>,
            required: false
        },
        app: {
            type: Object as PropType<App>,
            required: false
        },
        newApp: {
            type: Boolean,
            required: false,
            default: false
        }
    },
    emits: [
        'saveApp',
        'destroyApp'
    ],
    setup(props, ctx) {
        const app: AppSchema = reactive({
            name: "",
            apptype: "",
            csrfmiddlewaretoken: csrfToken?csrfToken:""
        });

        watch(props, ()=>{
            if(props.app){
                app.name = props.app.name;
                app.apptype = props.app.apptype.id;
            }
        })
        
        const disableSubmit = computed(()=>{
            return !validateAppSchema(app);
        })

        function saveApp(event: Event){
            event.preventDefault();
            if(validateAppSchema(app)){
                ctx.emit("saveApp", app);
            }
        }

        function destroyApp(){
            ctx.emit("destroyApp", app)
        }

        return {
            app,
            disableSubmit,
            saveApp,
            destroyApp
        }
    }
});
</script>