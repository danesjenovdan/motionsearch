import axios from 'axios'

const api = 'https://motion-search-backend.lb.djnd.si';

export const state = () => ({
  client_id:"NMBhhYpE4hOCFTxsgdHhKN0smPraXfd1sxsgLB2t",
  client_secret: "YmjUSqEplD67rCjg8mw0uWXlg7afEFRfgPWnE8l8XECgaYDvOxtbCYXBwQBuEDXTNRlZkkC1tFLpsv5tTWdngbQ8fx08n9vE4fcDnBWvwJEY8AEl8vb3MOwutvd33E5L",
  grant_type: "password",
  user: null,
  access_token: "",
  refresh_token : "",
  motion_length: 0,
  filters: {},
  filterCount: 0,
  motion: {},
  motionUpdate: 0
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
  motion_length (state) {
    return state.motion_length
  },
  getFilters (state) {
    return state.filters
  },
}

export const mutations = {
  refresh_token (state, token) {
    state.refresh_token = token
  },
  access_token (state, token) {
    state.access_token = token
  },
  motion_length (state, count) {
    state.motion_length = count;
  }
}


const mapFilters = (filters) => {
  let filterString = ''
  Object.keys(filters).forEach((key, index) => {
    if(index !== 0) filterString += '&'
    if (key === 'ageFilter') filterString += 'age_range='
    if (key === 'formatFilter') filterString += 'debate_formats='
    if (key === 'difficultyFilter') filterString += 'difficulties='
    if (key === 'typeFilter') filterString += 'type='
    if (key === 'trainingFilter') filterString += 'training_focus='
    if (key === 'improPrepFilter') filterString += 'impro_prep='
    if (key === 'id') filterString += 'id='

    filters[key].forEach((value, index) => {
      filterString += (index+1) !== filters[key].length ? value + ',' : value  
    })
  })
  return filterString
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
  async getMotionLength ({ getters }) {
    return getters.motion_length
  },

  async logout () {
    await this.$auth.logout()
  },

  async getMotions ({ getters, commit }, payload) {
    try {
      // https://motion-search-backend.lb.djnd.si/api/v1/motions/
      const filters = mapFilters(getters.getFilters)
      const result = await fetch(`${api}/api/v1/motions/?page=${payload.page}&${filters}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json'
          }
        })
      const body = await result.json(); // .json() is asynchronous and therefore must be awaited
      commit('motion_length', body.count);
      return body.results;
    } catch (error) {
      console.log(error);
    }
  },
  async getMotion (context, payload) {
    try {
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
  async postMotion ({ getters }, payload) {
    const response = await fetch(`${api}/api/v1/motions/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getters.access_token}`
      },
      body: JSON.stringify(payload) // body data type must match "Content-Type" header
    });
    const body = await response.json()
    console.log('body: ', body);
    return body
  },
  async getComments (context, payload) {
    try {
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
  async upvote ({ getters }, payload) {
    const response = await fetch(`${api}/api/v1/motions/${payload.id}/votes/`, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getters.access_token}`
      },
      body: JSON.stringify({
        choices: payload.choice,
      }) // body data type must match "Content-Type" header
    });
    const body = await response.json()
    console.log('body: ', body);
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
  async getMotionAttributes (context, payload) {
    let filters = ''
    if (payload.filters) filters = mapFilters(payload.filters)
    try {
      let next = `${api}/api/v1/motions/${payload.type}?page=1&${filters}`;
      let results = []; 
      while (next) {
        const result = await fetch(next, {
            method: 'get',
            headers: {
              'content-type': 'application/json'
            }
          })
        
        const body = await result.json();
        next = body.next;
        results = [...results, ...body.results];
      }
      return results;
    } catch (error) {
      console.log(error);
    }
  },

}

const store = {
  state,
  mutations,
  actions,
  getters
}

export default store

