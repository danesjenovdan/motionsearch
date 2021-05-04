import axios from 'axios'

const api = 'http://localhost:8000' || 'https://motion-search-backend.lb.djnd.si'

export const state = () => ({
  client_id:"NMBhhYpE4hOCFTxsgdHhKN0smPraXfd1sxsgLB2t",
  client_secret: "YmjUSqEplD67rCjg8mw0uWXlg7afEFRfgPWnE8l8XECgaYDvOxtbCYXBwQBuEDXTNRlZkkC1tFLpsv5tTWdngbQ8fx08n9vE4fcDnBWvwJEY8AEl8vb3MOwutvd33E5L",
  grant_type: "password",
  user: null,
  access_token: "",
  refresh_token : ""
})

export const getters = {
  access_token (state) {
    return state.access_token
  },
  refresh_token (state) {
    return state.refresh_token
  },
  client_secret (state) {
    return state.client_secret
  },
  client_id (state) {
    return state.client_id
  },
  grant_type (state) {
    return state.grant_type
  },
}

export const mutations = {
  refresh_token (state, token) {
    state.refresh_token = token
  },
  access_token (state, token) {
    state.access_token = token
  },
}

export const actions = {
  async login ({ getters, commit }, payload) {
    const response = await fetch(`${api}/auth/token/`, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: payload.username,
        password: payload.password,
        client_id: getters.client_id,
        client_secret: getters.client_secret,
        grant_type: getters.grant_type
      }) // body data type must match "Content-Type" header
    });
    const body = await response.json()
    commit('access_token', body.access_token);
    commit('refresh_token', body.refresh_token);
    return body
  },
  async isAuth ({ getters }) {
    return getters.access_token ? true : false
  },

  async logout () {
    await this.$auth.logout()
  },
  async getMotions (context, payload) {
    try {
      // https://motion-search-backend.lb.djnd.si/api/v1/motions/
      const result = await fetch(`${api}/api/v1/motions/?page=${payload.page}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json'
          }
        })
      const body = await result.json(); // .json() is asynchronous and therefore must be awaited
      return body.results;
    } catch (error) {
      console.log(error);
    }
  },
  async getMotion (context, payload) {
    console.log('payload: ', payload);
    try {
      // https://motion-search-backend.lb.djnd.si/api/v1/motions/
      const result = await fetch(`${api}/api/v1/motions/${payload.id}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json'
          }
        })
      const body = await result.json(); // .json() is asynchronous and therefore must be awaited
      return body;
    } catch (error) {
      console.log(error);
    }
  },
  async getComments (context, payload) {
    try {
      // https://motion-search-backend.lb.djnd.si/api/v1/motions/
      const result = await fetch(`${api}/api/v1/motions/${payload.id}/comments`, {
          method: 'get',
          headers: {
            'content-type': 'application/json'
          }
        })
      const body = await result.json(); // .json() is asynchronous and therefore must be awaited
      return body;
    } catch (error) {
      console.log(error);
    }
  },
  async setComment ({ getters }, payload) {
    console.log('payload: ', payload);
    const response = await fetch(`${api}/api/v1/motions/${payload.id}/comments/`, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getters.access_token}`
      },
      body: JSON.stringify({
        text: payload.text,
      }) // body data type must match "Content-Type" header
    });
    const body = await response.json()
    return body
  },
  async register (context, payload) {
    const response = await fetch(`${api}/api/v1/users/`, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: payload.username,
        email: payload.email,
        password: payload.password,
        phone_number: payload.phone
      }) // body data type must match "Content-Type" header
    });
    const body = await response.json()
    return body
  },

  async resetPassword (context, payload) {
    await axios.post('v1/restore-password/', {
      email: payload.email
    })
  },



}

const store = {
  state,
  mutations,
  actions,
  getters
}

export default store

