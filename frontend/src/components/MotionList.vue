<template>
  <div class="parent-container">
    <div class="header">
      <div class="logo">
        <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
      </div>
      <div class="header-buttons">
        <router-link to="/motionSuggest" class="btn">Suggest a motion</router-link>
        <router-link  v-show="!isAuth" to="/login" class="btn login">Log in</router-link>
      </div>
    </div>
    <div class="line"/>
    <div class="motions-container">
      <div class="motions-title-bar">
        <div>
          <h3>Motions</h3>
          <button class="btn" @click="toggleFilters">Filters</button>
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
      <div class="motions-list" v-for="motion in motions" :key="motion.id">
        <div class="motion-text-container">
          <p class="motions-date">Added on {{motion.created_at.split('T')[0]}}</p>
          <a :href="'/motion/'+motion.id" class="motions-title">{{motion.topic}}</a>
        </div>
        <div class="votes">
          <voting :votes="motion.votes" :id="motion.id"/>
        </div>
      </div>
    </div>
    <div class="pagination">
      <div>
        <button @click="changeSite(1)">
          <svg width="15" height="15" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:avocode="https://avocode.com/" viewBox="0 0 15 15"><defs></defs><desc>Generated with Avocode.</desc><g><g><title>noun_chevron_2286633 copy</title><image xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAABRUlEQVQ4T33TzyunURQG8I8Vq7GympHZkJoampSmNNhY2TELKavRZCFZSBYaRbLAQrJhh1kwO6vJhomSEjaT0dTkR03zN0yiq/Pq7dv7dVe3c5/nnOc859wK5U8TDvEZmznYGGbQXlGG24Bf8daCk7j34SvO0FNEfo0/uEMt/gaxB9+wj44UKyW/xG2AU5KruHdjB8dozdTmyTW4QSXq8TtAXfiOczTn28zI1bjGC7zBzwC1Yw+XaMR9KbkOu1HtHU6jnQ9BvMBb/C81N1VOriZ33+MoAK+ihSJfnnIkci+2Y6adUaEK45jCEkaKRpr1nCSmEZT2lhLMYQ2DRbKzWDlXv4SCZQwXuZ3FCueJWUxgHmk9H0/RhmUe/Ej7m6u0iNHY68nnnOzHBg7C0H+RZAVDWMB0uY+RsJ+wigGs5xRs4SPaHgAT/z+0+ejOmgAAAABJRU5ErkJggg==" width="15" height="15" transform="matrix(1,0,0,1,0,0)" ></image></g></g></svg>
        </button>
        <button @click="changeSite(page - 1)">
          <svg width="9" height="16" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:avocode="https://avocode.com/" viewBox="0 0 9 16"><defs></defs><desc>Generated with Avocode.</desc><g><g><title>noun_chevron_2286605</title><image xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAQCAYAAADESFVDAAAAbElEQVQoU53SwQmAMAyF4b8buIxHBxCcwJObOYWu4EVwpRIhIDFJxZ6/9iVNCvmZga4kZgR24IqQggMYPKTgBHpJsugFLHLBE4VA0QKswAZMXrdS0yckl5txmtAsPIW/PtO+GI7FwnDACu9VqZ6vHIcNAterAAAAAElFTkSuQmCC" width="9" height="16" transform="matrix(1,0,0,1,0,0)" ></image></g></g></svg>
        </button>
        <ul>
          <li v-for="p in pagesNo" key="p" :class="{'active-page': p === page}" @click="changeSite(p)">{{p}}</li>
          <!--
          <li class="active-page">1</li>
          <li>2</li>
          <li>3</li>
          <li class="disabled">...</li>
          <li>9</li>
          -->
        </ul>
        <button @click="changeSite(page + 1)">
          <svg width="8" height="15" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:avocode="https://avocode.com/" viewBox="0 0 8 15"><defs></defs><desc>Generated with Avocode.</desc><g><g><title>noun_chevron_2286605 copy</title><image xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAPCAYAAADZCo4zAAAAs0lEQVQoU3XRIWuCURTG8Z9p4AfR4ldYM70Y1lbWDAoaDLIos24YBsoWrJY1gxisxsGCZfsgwzg54IWXy91p9/I//wfO08AZL5gpTAM/aOEBm5wJIOaALu6wrUMJiL8TOrjHR4LqQBNf17gK+4DqQLxv8Hk13eKYA8n8jTaq/4CI+y1FJMM7BnguGZYYYYpFDqzRxxxPeUTSvmKS3yF6iK3o5DG/5BuGWGFc6uIPO/RKbV4A0xUb4dD0ryEAAAAASUVORK5CYII=" width="8" height="15" transform="matrix(1,0,0,1,0,0)" ></image></g></g></svg>
        </button>
        <button @click="changeSite(pagesNo)">
          <svg width="15" height="15" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:avocode="https://avocode.com/" viewBox="0 0 15 15"><defs></defs><desc>Generated with Avocode.</desc><g><g><title>noun_chevron_2286633</title><image xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAA+ElEQVQ4T5XTvyuHQRwH8Ne3TFabxB+gKDEpk0UMfvwJJoxSBiYMpJTJ4E/wYxDFioXFbCKDRUaLkq7uct+ne756brque70/93meuxaGcIAlPPsbK5jEXLbWNm1hGE/4QR/e445FHOMWE6WAgMPox2shYBbndQEJdwoIxz4rBeS4cUAVNwoo4RAwgBd8YARv8dvM4xTXmKrDYW8XviPqwWecz+AC953wGvZwhFV8RXyCBSzX4f0ItrGZ/eNHjGIaVyWc4A42MviAsQTDehX/B0O/lykwx41gqtyNQ4S7nPfYixsMoq1iXnkcd9jFetZj6Hcr77H6OH4BUthBPqob+J4AAAAASUVORK5CYII=" width="15" height="15" transform="matrix(1,0,0,1,0,0)" ></image></g></g></svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
  import Voting from './Voting.vue'

  export default {
    props: ['id'],
    data() {
      return {
        motions: [],
        page: 1,
        refresh: true,
        isAuth: false,
        motionsNo: 0,
        dateSortAscend: false,
        qualitySortAscend: false
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
            const result = await this.$store.dispatch('getMotions', {page: p})
            if (result) {
              this.motions = result
              this.page = p
            }
          } catch (error) {
            console.log(error)
          }
        }
      },
      /*
      async loadNextPage() {
        try {
          this.page += 1;
          const result = await this.$store.dispatch('getMotions', {page: this.page})
          if(result) this.motions = this.motions.concat(result)
          else this.page -= 1
          this.refresh = true
        } catch (error) {
          this.refresh = true
        }
      },
      handleScroll(e) {
        // compare height of motions-container to window height to enable next scrolling
        let element = document.querySelector('.motions-container')
        if ( element.getBoundingClientRect().bottom < window.innerHeight && this.refresh) {
          this.loadNextPage()
          this.refresh = false
        }
      },
      */
      toggleFilters() {
        this.$emit('toggle-filters')
      },
      toggleDateSort() {
        this.dateSortAscend = !this.dateSortAscend
      },
      toggleQualitySort() {
        this.qualitySortAscend = !this.qualitySortAscend
      }
    },
    watch: {
      '$store.state.motions.filterCount': async function() {
        this.motions = await this.$store.dispatch('getMotions', {page: 1, filters: this.$store.state.motions.filters})
      }
    },
    /*
    mounted() {
      window.addEventListener("scroll", this.handleScroll)
    },
    unmounted() {
      window.removeEventListener("scroll", this.handleScroll)
    },
    */
    async created() {
      this.isAuth = await this.$store.dispatch('isAuth')
      this.motions = await this.$store.dispatch('getMotions', {page: 1})
      this.motionsNo = await this.$store.dispatch('getMotionLength')
      console.log(this.motionsNo)
    }
  }

</script>

<style scoped lang="scss">

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;

  @media (min-width: 768px) {
    justify-content: flex-end;
    padding: 20px;
  }

  @media (min-width: 1200px) {
    padding: 30px;
  }

  .logo {
    @media (min-width: 768px) {
      display: none;
    }

    img {
      height: 40px;
    }
  }
}

.motions-container {
  display: flex;
  flex-direction: column;
  // overflow: hidden;
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
      font-size: 16px;
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

      @media (min-width: 768px) {
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
        font-size: 24px;
        text-decoration: none;
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
