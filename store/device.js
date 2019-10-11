import gql from 'graphql-tag'

export const state = () => ({
    item:{},
    stale:false,
    loading: 0,
    networkStatus : 0
  })
  
export const mutations = {

  setitem(state, item) {
    state.item = item
  },

  clearitem(state) {
    state.item = {}
  },

  loading(state,isLoading) {
    state.loading = isLoading
  },

  stale(state,isStale) {
    state.stale = isStale
  },

  networkStatus(state,statiusCode) {
    state.networkStatus = statiusCode
  }
}

export const getters = {

    item: state => {
        return state.item
    },

    loading: state => {
        return state.loading
    },
}

export const actions = {
  
  async fetch({ commit }, id){

    let client = this.app.apolloProvider.defaultClient
       
    commit('loading', 1 );

    await client.query({ 
      query: gql`query device($id: uuid!){
        devices_by_pk(id: $id ) {
          weight 
        }
      }`,

      variables: {id:id},

      fetchPolicy: 'network-only'

    }).then((response) => { 
        console.log(response)
        commit('clearitem');
        commit('setitem',  response.data.devices_by_pk );
        commit('loading', 0 );
        commit('stale', response.data.stale );
        commit('networkStatus', response.data.networkStatus );
     })

  },

  async observe({ commit }){
       
    let client = this.app.apolloProvider.defaultClient

    await client.subscribe({ 

      query: gql`subscription device($id: uuid!) {
          devices_by_pk(id: $id) {
            id
            weight
          }
        }`,

      variables: {id:"1eb6aa14-4004-4a57-a0aa-dbf7a837c992"},

      fetchPolicy: 'network-only'

    }).subscribe({
      next (response) {
        console.log(response)
        commit('clearitem');
        commit('setitem', response.data.devices_by_pk);    
      },
      error (error) {
        console.error(error)
      }
    })
  }
}