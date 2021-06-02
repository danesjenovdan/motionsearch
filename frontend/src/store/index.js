import axios from 'axios'
import { useToast } from "vue-toastification";
import IconComponent from "../components/IconComponent.vue"

const toast = useToast();

const api = 'https://motion-search-backend.lb.djnd.si';

export const state = () => ({
  client_id:"NMBhhYpE4hOCFTxsgdHhKN0smPraXfd1sxsgLB2t",
  client_secret: "YmjUSqEplD67rCjg8mw0uWXlg7afEFRfgPWnE8l8XECgaYDvOxtbCYXBwQBuEDXTNRlZkkC1tFLpsv5tTWdngbQ8fx08n9vE4fcDnBWvwJEY8AEl8vb3MOwutvd33E5L",
  grant_type: "password",
  user: null,
  access_token: "",
  refresh_token : "",
  token_expiration: '',
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
  token_expiration (state) {
    return state.token_expiration
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
  token_expiration (state, token) {
    state.token_expiration = token
  },
  motion_length (state, count) {
    state.motion_length = count;
  }
}

const mapUsersToComments = async(context, comments, userIDs) => {
  const filterString = `id=${Array.from(userIDs).join(',')}`
  const users = await actions.getUsers(context, {filterString})
  comments.map((comment) => comment.user = users.results.find((user) => user.id === comment.user))
  return comments
}

const mapFilters = (filters) => {
  let filterString = ''
  Object.keys(filters).forEach((key, index) => {
    if(index !== 0) filterString += '&'
    if (key === 'categoryFilter') filterString += 'category='
    if (key === 'ageFilter') filterString += 'age_range='
    if (key === 'formatFilter') filterString += 'debate_formats='
    if (key === 'difficultyFilter') filterString += 'difficulties='
    if (key === 'typeFilter') filterString += 'type='
    if (key === 'trainingFilter') filterString += 'training_focus='
    if (key === 'improPrepFilter') filterString += 'impro_prep='
    if (key === 'id') filterString += 'id='
    if (key === 'ordering') filterString += 'ordering='
    if (key === 'keywordFilter') filterString += 'topic='

    if(Array.isArray(filters[key])) {
      filters[key].forEach((value, index) => {
        if(!value.id) filterString += (index+1) !== filters[key].length ? value + ',' : value
        else filterString += (index+1) !== filters[key].length ? value.id + ',' : value.id
      })
    } else {
      filterString += filters[key]
    }

  })
  return filterString
}

Date.prototype.addHours = function(h) {
  this.setTime(this.getTime() + (h*60*60*1000));
  return this;
}

export const actions = {
  async login ({ getters, commit }, payload) {
    try {
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
      if(body.error) {
        commit('access_token', null);
        commit('refresh_token', null);
        commit('token_expiration', null);
        toast.error(`Could not login: ${body.error_description}`);
        return false
      }
      commit('access_token', body.access_token);
      commit('refresh_token', body.refresh_token);
      commit('token_expiration', new Date().addHours(10));
      toast.success("Succesfully loged in.");
      return body
    } catch (error) {
      toast.error("Could not log in. Please try again");
      return error
    }
  },
  async checkAndRefreshToken(context) {
    if(new Date() > context.getters.token_expiration) {
      return this.refreshToken(context)
    } else return true;
  },
  async refreshToken ({getters, commit}) {
    const response = await fetch(`${api}/auth/token/`, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        token_type:"bearer",
        access_token: getters.access_token,
        refresh_token: getters.refresh_token,
        client_id: getters.client_id,
        client_secret: getters.client_secret,
        grant_type: "refresh_token"
      }) // body data type must match "Content-Type" header
    });
    const body = await response.json()
    commit('access_token', body.access_token);
    commit('refresh_token', body.refresh_token);
    commit('token_expiration', new Date().addHours(10));

    return body
  },

  async isAuth ({ getters }) {
    return getters.access_token ? true : false
  },
  async getMotionLength ({ getters }) {
    return getters.motion_length
  },

  async logout () {
    try {
      await this.$auth.logout()
      toast.success("Succesfully loged out.");
    } catch (error) {
      toast.error("There was a problem, with logging out.");
      return error
    }
  },
  async getMe ({ getters, commit }, payload) {
    try {
      const filters = mapFilters(getters.getFilters)
      const result = await fetch(`${api}/api/v1/users/me/`, {
          method: 'get',
          headers: {
            'content-type': 'application/json',
            'Authorization': `Bearer ${getters.access_token}`
          }
        })
      return await result.json();
    } catch (error) {
      return error
    }
  },
  async getUsers ({ getters, commit }, payload) {
    try {
      const result = await fetch(`${api}/api/v1/users?${payload.filterString}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json',
            'Authorization': `Bearer ${getters.access_token}`
          }
        })
      return await result.json();
    } catch (error) {
      return error
    }
  },
  async getMotions ({ getters, commit }, payload) {
    try {
      const filters = mapFilters(getters.getFilters)
      const result = await fetch(`${api}/api/v1/motions/?page=${payload.page}&${filters}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json'
          }
        })
      return await result.json();
    } catch (error) {
      return error
    }
  },
  async getMyMotions ({ getters, commit }, payload) {
    try {
      let response = await fetch(`${api}/api/v1/users/me/motions?page=${payload.page}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json',
            'Authorization': `Bearer ${getters.access_token}`
          }
        })
      response = await response.json();
      const idArray = response.map(motion => motion.id)
      const filters = mapFilters({id:idArray, ...payload.filters})
      response = await fetch(`${api}/api/v1/motions/?page=${payload.page}&${filters}`, {
        method: 'get',
        headers: {
          'content-type': 'application/json'
        }
      })
      return await response.json();
    } catch (error) {
      return error
    }
  },
  async getMyFavorites ({ getters, commit }, payload) {
    try {
      const filters = mapFilters(getters.getFilters)
      const result = await fetch(`${api}/api/v1/users/me/favorites?page=${payload.page}&${filters}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json'
          }
        })
      return await result.json();
    } catch (error) {
      return error
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
      return error
    }
  },
  async postMotion ({ getters, commit }, payload) {
    //payload.user = 0
    await actions.checkAndRefreshToken({ getters, commit })
    try {
      const response = await fetch(`${api}/api/v1/motions/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${getters.access_token}`
        },
        body: JSON.stringify(payload) // body data type must match "Content-Type" header
      });
      const body = await response.json()
      toast.success("Succesfully posted a motion.");
      return body
    } catch (error) {
      toast.error("There was an error with posting motion.");
      return error
    }
  },
  async getFavorites ({ getters }, payload) {
    const response = await fetch(`${api}/api/v1/users/me/favorites`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getters.access_token}`
      },
    });
    const body = await response.json()
    return body
  },
  async getFavoritesMotions ({ getters, commit }, payload) {
    try {
      await actions.checkAndRefreshToken({ getters, commit })
      let response =  await actions.getFavorites({ getters }, payload)
      const idArray = response.map(favorite => favorite.motion)
      const filters = mapFilters({id:idArray, ...payload.filters})
      response = await fetch(`${api}/api/v1/motions/?page=${payload.page}&${filters}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json'
          }
        })
      return await response.json();
    } catch (error) {
      console.log(error);
    }
  },
  async postFavorite ({ getters, commit }, payload) {
    await actions.checkAndRefreshToken({ getters, commit })
    try {
      const response = await fetch(`${api}/api/v1/users/1/favorites/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${getters.access_token}`
        },
        body: JSON.stringify(payload) // body data type must match "Content-Type" header
      });
      const body = await response.json()
      toast.success("Motion was favorited successfully.");
      return body      
    } catch (error) {
      toast.error("Could not save favorite motion.");
      return error
    }
  },
  async deleteFavorite ({ getters, commit }, payload) {
    await actions.checkAndRefreshToken({ getters, commit })
    try {
      const response = await fetch(`${api}/api/v1/users/1/favorites/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${getters.access_token}`
        },
        body: JSON.stringify(payload) // body data type must match "Content-Type" header
      });
      const body = await response.json()
      toast.success("Motion was unfavorited successfully");
      return body
    } catch (error) {
      toast.error("Could not save favorite motion.");
      return error
    }
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
      let uniqueUsers = new Set()
      body.forEach((obj) => {
        uniqueUsers.add(obj.user)
      })
      const comments = mapUsersToComments(context, body, uniqueUsers);
      return comments;
    } catch (error) {
      console.log(error);
    }
  },
  async setComment ({ getters, commit }, payload) {
    await actions.checkAndRefreshToken({ getters, commit })
    try {
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
      toast.success("Comment was submited successfully");
      return body
    } catch (error) {
      console.log('error: ', error);
      toast.error("Could not post comment");
      return error
    }
  },
  async upvote ({ getters, commit }, payload) {
    await actions.checkAndRefreshToken({ getters, commit })
    try {
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
      toast.success('Succesfully voted on motion.')
      const body = await response.json()
      return body
    } catch (error) {
      toast.error('There was a problem with casting a vote.')
      return error
    }
  },
  async getUpvotes ({ getters }, payload) {
    const response = await fetch(`${api}/api/v1/users/me/votes`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getters.access_token}`
      },
    });
    const body = await response.json()
    return body
  },
  async register (context, payload) {
    try {
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
      toast.success("Registration completed successfully. Check email to confirm address.");
      const body = await response.json()
      return body
      
    } catch (error) {
      toast.success("Registration could not be completed");
      return error
    }
  },
  async reset (context, payload) {
    try {
      const response = await fetch(`${api}/api/v1/users/forgot-password/`, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: payload.email,
        })
      });
      const body = await response.json()
      toast.info("Password reset link, was sent to your email account.");
      return body
    } catch (error) {
      toast.error("Password change was not possible");
      return error
    }
  },

  async change (context, payload) {
    try {
      const response = await fetch(`${api}/api/v1/users/change-password/${payload.uid}/${payload.token}/`, {
        method: 'PUT', // *GET, POST, PUT, DELETE, etc.
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          password: payload.password,
        })
      });
      const body = await response.json()
      toast.success("Password was successfully changed.");
      return body
    } catch (error) {
      toast.error("Password change was not possible");
      return error
    }
  },

  async resetPassword (context, payload) {
    try {
      await axios.post('v1/restore-password/', {
        email: payload.email
      })
      toast.info("Password reset link, was sent to your email account.");
    } catch (error) {
      toast.error("Password change was not possible");
      return error
    }
  },
  async getMotionAttributes (context, payload) {
    let filters = ''
    if (payload.filters) filters = mapFilters(payload.filters)
    try {
      console.log('`${api}/api/v1/motions/${payload.type}?page=1&${filters}`: ', `${api}/api/v1/motions/${payload.type}?page=1&${filters}`);
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
        next = next?.includes('http://') ? next.replace('http://', 'https://') : next
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

