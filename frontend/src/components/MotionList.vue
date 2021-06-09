<template>
  <div v-if="motions.length > 0 || hideAll" class="parent-container">
    <div v-if="headers" class="header">
      <div class="logo">
        <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
      </div>
      <div class="header-buttons">
        <router-link to="/motionSuggest" class="button button--suggest"><span>Suggest a motion</span></router-link>
        <router-link to="/login" v-if="!isAuth"  class="button button--pan"><span>Log in</span></router-link>
        <router-link to="/profile" v-if="isAuth" class="button button--pan"><span>Profile</span></router-link>
      </div>
    </div>
    <div v-if="headers" class="line"/>
    <div class="motions-container">
      <div class="motions-title-bar">
        <div>
          <h3>{{title}}</h3>
          <button v-if="headers" class="btn" @click="toggleFilters">Filters</button>
        </div>
        <div class="motions-sort">
          <p>Sort by</p>
          <div class="sort-button" @click="toggleDateSort">
            <span>Date Added</span>
            <svg :class="{'toggled': dateSortAscend}" width="13" height="15" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:avocode="https://avocode.com/" viewBox="0 0 13 15"><defs></defs><desc>Generated with Avocode.</desc><g><g><title>down-arrow_2796734</title><image xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPCAYAAAA/I0V3AAAAvklEQVQ4T83SIW4CQRQA0LfBkTQguAOmSXFwAWQVjiNUNHCCOgQCJB7BBfC4+vYGKARp0opq0gzZbYZllqxk3Pz8NzP//8mkVxNdfOJUTskq0AeesMJLHdTCT54YburVQW183w/q4A0HzPGQeF6Rc8QsdG+JSV7DBq/4imoaYofHPDYKaIpF1KEtnvP9Hr8RCOF+QA2sMa6YWRwOM1sVw60DzyCcEP+IW/AflFHYp+AFSKEyvAJVqIADvKea8wd56yabc1zKQwAAAABJRU5ErkJggg==" width="13" height="15" transform="matrix(1,0,0,1,0,0)" ></image></g></g></svg>
          </div>
          <div class="sort-button" @click="toggleQualitySort">
            <span>Quality</span>
            <svg :class="{'toggled': qualitySortAscend}" width="13" height="15" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:avocode="https://avocode.com/" viewBox="0 0 13 15"><defs></defs><desc>Generated with Avocode.</desc><g><g><title>down-arrow_2796734</title><image xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPCAYAAAA/I0V3AAAAvklEQVQ4T83SIW4CQRQA0LfBkTQguAOmSXFwAWQVjiNUNHCCOgQCJB7BBfC4+vYGKARp0opq0gzZbYZllqxk3Pz8NzP//8mkVxNdfOJUTskq0AeesMJLHdTCT54YburVQW183w/q4A0HzPGQeF6Rc8QsdG+JSV7DBq/4imoaYofHPDYKaIpF1KEtnvP9Hr8RCOF+QA2sMa6YWRwOM1sVw60DzyCcEP+IW/AflFHYp+AFSKEyvAJVqIADvKea8wd56yabc1zKQwAAAABJRU5ErkJggg==" width="13" height="15" transform="matrix(1,0,0,1,0,0)" ></image></g></g></svg>
          </div>
        </div>
      </div>
      <ul class="tags">
        <li class="tag" v-for="tag, index in tags" :key="tag.id">
          <span class="tag-text">{{ tag.filterValue.value }} <img  v-on:click="removeFilter(tag.filterValue.value, tag.filter, index)" src="../assets/x.svg"/></span>
        </li>
      </ul>
      <div v-if="motions.length > 0" class="motions-list" v-for="motion in motions" :key="motion.id">
        <div class="motion-text-container">
          <p class="motions-date">Added on {{motion.created_at.split('T')[0]}}</p>
         <router-link :to="'/motion/'+motion.id" class="motions-title">{{motion.topic}}</router-link>
        </div>
        <div class="votes">
          <voting :votes="motion.votes" :id="motion.id" :choice="motion.choice"/>
        </div>
      </div>
    <div class="notFound" v-else>
      <img src="../assets/filters-not-found.svg"/>
      <span>No results found.<br>
        Please try different filters.
      </span>
    </div>
    </div>
    <div v-if="pagesNo > 1" class="pagination">
      <div>
        <button @click="changeSite(1)">
        <svg class="rotate-arrow" height='15' width='15'  fill="#000000" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24" version="1.1" x="0px" y="0px"><title>icon/double-chevron-right-solid</title><desc>Created with Sketch Beta.</desc><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><path d="M11.8789,2.6816 L13.2929,1.2676 L23.9999,11.9746 L13.2929,22.6816 L11.8789,21.2676 L21.1719,11.9746 L11.8789,2.6816 Z M5.293,22.6816 L3.879,21.2676 L13.172,11.9746 L3.879,2.6816 L5.293,1.2676 L16,11.9746 L5.293,22.6816 Z" fill="#000000"></path></g></svg>
        </button>
        <button @click="changeSite(page - 1)">
          <svg height='15' width='15'  fill="#000000" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24" version="1.1" x="0px" y="0px"><title>icon/chevron-left-solid</title><desc>Created with Sketch Beta.</desc><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><polygon fill="#000000" points="16.1211 21.2676 6.8281 11.9746 16.1211 2.6816 14.7071 1.2676 4.0001 11.9746 14.7071 22.6816"></polygon></g></svg>
        </button>
        <ul>
          <li v-for="p in pagesNo" :key="p" :class="{'active-page': p === page}" @click="changeSite(p)">{{p}}</li>
        </ul>
        <button @click="changeSite(page + 1)">
        <svg class="rotate-arrow" height='15' width='15'  fill="#000000" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24" version="1.1" x="0px" y="0px"><title>icon/chevron-left-solid</title><desc>Created with Sketch Beta.</desc><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><polygon fill="#000000" points="16.1211 21.2676 6.8281 11.9746 16.1211 2.6816 14.7071 1.2676 4.0001 11.9746 14.7071 22.6816"></polygon></g></svg>
        </button>
        <button @click="changeSite(pagesNo)">
        <svg height='15' width='15'  fill="#ffffff" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24" version="1.1" x="0px" y="0px"><title>icon/double-chevron-right-solid</title><desc>Created with Sketch Beta.</desc><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><path d="M11.8789,2.6816 L13.2929,1.2676 L23.9999,11.9746 L13.2929,22.6816 L11.8789,21.2676 L21.1719,11.9746 L11.8789,2.6816 Z M5.293,22.6816 L3.879,21.2676 L13.172,11.9746 L3.879,2.6816 L5.293,1.2676 L16,11.9746 L5.293,22.6816 Z" fill="#000000"></path></g></svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
  import Voting from './Voting.vue'

  export default {
    props: ['id', 'type', 'title', 'headers', 'hideAll', 'propsMotions', 'category'],
    data() {
      return {
        motions: [],
        page: 1,
        refresh: true,
        isAuth: false,
        motionsNo: 0,
        dateSortAscend: false,
        qualitySortAscend: false,
        votes: [],
        tags: []
      }
    },
    computed: {
      pagesNo: function() {
        return Math.ceil(this.motionsNo/10)
      }
    },
    components: {
      Voting
    },
    methods: {
      async changeSite (p) {
        if (p > 0 && p <= this.pagesNo) {
          try {
            const response = await this.$store.dispatch(this.type, {page: p})
            if (response) {
              this.motions = response.results
              this.motionsNo = response.count
              await this.getUserVotes()
              this.page = p
            }
          } catch (error) {
            console.log(error)
          }
        }
      },
      async getUserVotes() {
        this.votes = await this.$store.dispatch('getUpvotes')
        this.motions.forEach(motion => {
          const choice = this.votes.find(vote => vote.motion === motion.id)
          if (choice) motion.choice = choice.choices;
       });
      },
      toggleFilters() {
        this.$emit('toggle-filters')
      },
      toggleDateSort() {
        this.dateSortAscend = !this.dateSortAscend
        this.$store.state.motions.filters['ordering'] = this.dateSortAscend ? 'created_at' : '-created_at'
        this.$store.state.motions.filterCount += 1
      },
      removeFilter(filter, type, index) {
        this.tags.splice(index, 1)
        this.$store.state.motions.filters[type] = this.$store.state.motions.filters[type].filter((obj) => obj.value !== filter);
        this.$store.state.motions.filterCount += 1
      },
      toggleQualitySort() {
        this.qualitySortAscend = !this.qualitySortAscend
        this.$store.state.motions.filters['ordering'] = this.qualitySortAscend ? 'votes' : '-votes'
        this.$store.state.motions.filterCount += 1
      }, mapFiltersToTags() {
        this.tags = []
        Object.keys(this.$store.state.motions.filters).forEach(filter => {
          if(filter !== 'keywordFilter' && filter !== 'ordering') this.$store.state.motions.filters[filter].forEach((filterValue) => {
            this.tags.push({filterValue, filter})
          })
        })
      }
    },
    watch: {
      '$store.state.motions.filterCount': async function() {
        await this.mapFiltersToTags()
        const response = await this.$store.dispatch(this.type, {page: 1, filters: this.$store.state.motions.filters})
        console.log('response: ', response);
        this.motions = response.results
        this.motionsNo = response.count
        await this.getUserVotes()
      }
    },
    async created() {
      this.$store.state.motions.filters = {} // clean filter if we have bad state or propfilters
      if(this.category ) { 
        this.$store.state.motions.filters.categoryFilter = [{id: this.category[1], value: this.category[0]}];
        }
      this.isAuth = await this.$store.dispatch('isAuth')
      let response = []
      console.log('this.type: ', this.type);
      if (!this.propsMotions) response = await this.$store.dispatch(this.type, {page: 1})
      this.motions = this.propsMotions ? this.propsMotions : response.results
      this.motionsNo = response.count
      await this.mapFiltersToTags()
      await this.getUserVotes()
    }
  }

</script>

<style scoped lang="scss">

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;

  @media (min-width: 992px) {
    justify-content: flex-end;
  }

  @media (min-width: 1200px) {
  }

  .logo {
    img {
      margin-left: 20px;
      height: 30px;

      @media (min-width: 576px) {
        height: 40px;
      }

      @media (min-width: 992px) {
        display: none;
      }
    }
  }

  .btn {
    @media (max-width: 575px) {
      padding: 5px 5px;
      font-size: 10px;
    }
  }
  .button {
    margin-left:10px;
    @media (max-width: 575px) {
      padding: 5px 5px;
      font-size: 10px;
    }
  }
}

.motions-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow-y: scroll;
  padding: 0 20px;
  margin-bottom: 20px;

  @media (min-width: 992px) {
    padding: 0 40px;
  }

  .motions-title-bar {
    display: flex;
    flex-direction: column;
    border-bottom: 1px solid black;

    @media (min-width: 992px) {
      flex-direction: row;
      justify-content: space-between;
    }

    div:nth-child(1) {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 0;

      @media (min-width: 992px) {
        padding: 20px 0;
      }
    }

    h3 {
      font-size: 20px;
      margin: 0;
      color: #252525;
      font-family: "Poppins";

      @media (min-width: 768px) {
        font-size: 30px;
        line-height: 60px;
      }
    }

    button {
      font-size: 14px;
      letter-spacing: 1px;
      padding: 5px 12px;

      @media (min-width: 992px) {
        display: none;
      }
    }

    .motions-sort {
      display: flex;
      flex-direction: row;
      align-items: center;
      margin-bottom: 10px;

      @media (min-width: 992px) {
        margin-bottom: 0;
      }

      .sort-button, p {
        font-family: "IBM Plex Mono";
        font-size: 12px;
        line-height: 14px;

        @media (min-width: 992px) {
          font-size: 14px;
          line-height: 18px;
        }
      }

      .sort-button {
        border-radius: 20px;
        background-color: rgb(48, 152, 243, 0.2);
        padding: 5px 10px;
        margin-left: 10px;
        cursor: pointer;
        color: #000000;
        font-weight: 700;
        text-transform: uppercase;
        display: flex;
        align-items: center;

        svg {
          margin-left: 0.5rem;
          transition: transform 0.5s;
          height: 14px;
          &.toggled {
            transform: rotate(-180deg);
          }
        }
      }
      .sort-button:hover {
        background-color:  #ffcc00;
      }
    }
  }
  .motions-list {
    border-bottom: 1px solid black;
    padding: 0.5rem 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    // width: 100%;

    .motion-text-container {
      display: flex;
      flex-direction: column;
      color: #252525;
      margin: 1rem 0;

      .motions-date {
        font-family: "IBM Plex Mono";
        font-size: 14px;
        font-style: italic;
        line-height: 18px;
        margin: 0 0 0.25rem;
      }

      .motions-title {
        color: #252525;
        font-family: Poppins;
        font-size: 20px;
        text-decoration: none;
        @media (min-width: 992px) {
          font-size: 24px;
        }
      }
      .motions-title:hover {
        color: #3098f3;
      }
    }

    .votes {
      width: 78px;
      height: 78px;
      flex-shrink: 0;
      // margin-right: 20px;
      margin-left: 20px;
      background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%);
    }
  }
  .notFound {
    display: flex;
    flex-direction: column;
    img {
      margin-top: 50px;
      width: 80px;
      margin-left: auto;
      margin-right: auto;
    }

    span {
    color: #252525;
    font-family: Poppins;
    font-size: 20px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 30px;
    text-align: center;
    }
  }
}

.share-bar {
  position: relative;
  width: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: row;
  padding: 20px;
  // background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
  background-image: linear-gradient(-62deg, #cee7fd 0%, #f7fafd 100%);
  z-index: 2;

  .share-bar-split {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: center;
    &.hidden {
      display: none !important;
    }
  }

  h1 {
      margin-top: 0;
      // width: 100%;
  }

  input {
      margin-left: 20px;
  }
}

.parent-container {
  display: flex;
  width: 100%;
  margin: 0 auto;
  flex-direction: column;
  justify-content: center;
  align-items: initial;
  overflow-x: auto;
}

.favourite{
  background-image: '../assets/favourite.svg';
}

.motionButtons {
  display: flex;
  justify-content: space-between;
}

.line {
  margin: 0;
  border-top: 1px solid #3098f3;
}

</style>
