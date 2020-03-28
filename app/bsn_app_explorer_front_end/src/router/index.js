import Vue from 'vue'
import Router from 'vue-router'
import transactions from '@/components/transaction'
import data_on_chain from '@/components/data_on_chain'
import index from '@/components/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/data_on_chain',
      name: 'data_on_chain',
      component: data_on_chain
    },
    {
      path: '/transactions',
      name: 'transactions',
      component: transactions
    },
  ]
})
