import { api } from '@/utils/api.js'
import store from '@/store/index'

export function graud (to, from, next) {
    api('query{ me { id, isSuperuser, username, firstName, lastName, profile{ team { name } } } }').then(data => {
        if(data.me !== null) {
            store.commit('user/SET_USER', data.me)
            next();
        } else {
            console.log("[ROUTE]: Authenication failed, going to login")
            next('/login');
        }
    })
}

export function superusergraud (to, from, next) {
    api('query{ me { id, isSuperuser, username, firstName, lastName, profile{ team { name } } } }').then(data => {
        if(data.me !== null) {
            store.commit('user/SET_USER', data.me)
            data.me.isSuperuser ? next() : next('/');
            next();
        } else {
            console.log("[ROUTE]: Authenication failed, going to login")
            next('/login');
        }
    })
}