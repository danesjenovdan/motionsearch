<template>
<div class="background container">
  <div class="header">
    <div class="logo">
        <router-link to="/"><img src="../assets/motion-generator-logo.svg" alt="motion generator logo"></router-link>
      <span>Easiest way to find a motion for debating</span>
    </div>
    <div class="header-buttons">
      <router-link to="/motionSuggest" class="button button--suggest"><span>Suggest a motion</span></router-link>
      <router-link to="/login" v-if="!isAuth" class="button button--pan"><span>Log in</span></router-link>
      <router-link to="/profile" v-if="isAuth" class="button button--pan"><span>Profile</span></router-link>
    </div>
  </div>
  <div class="wrapper">
    <div class="motionSuggestContainer">
      <h1>Suggest a motion</h1>
        <form @submit="postMotion">
          <div class="textAreaContainer">
            <label>Topic</label><br>
            <textarea rows="3" cols="20" name="topic" ref="topic"></textarea>
          </div>
          <div class="inputContainer">
            <label >Category</label>
              <div class="arrayContainer">
                <div class="linkContainer" v-for="(element, index) in chosenCategory" :element="element" :key="element" :vid-id="index">
                    <span v-on:click="removeCategory(index)"><img src="../assets/x.svg"/></span>{{categoryOptions[element]}}
                </div>
              <div class="select-wrapper-full">
                <select v-model="categories" name="Category" id="categories">
                  <option v-for="(value, id) in categoryOptions" v-bind:key="id" :value="id">{{value}}</option>
                </select>
              </div>
              </div>
          </div>
          <div class="inputContainer">
            <label>Difficulty</label>
            <div class="select-wrapper">
              <select v-model="difficulty" name="Dificulty" id="difficulty">
                <option v-for="difficulty in difficultiesOptions" v-bind:key="difficulty" :value="difficulty.id">{{difficulty.value}}</option>
              </select>
            </div>
          </div>
          <div class="inputContainer">
            <label>Debate format</label>
            <div class="select-wrapper">
              <select v-model="debateFormat" name="DebateFormat" id="debateFormat">
                <option v-for="debateFormat in debateFormatOptions" v-bind:key="debateFormat" :value="debateFormat.id">{{debateFormat.value}}</option>
              </select>
            </div>
          </div>
          <div class="inputContainer">
            <label >Age</label>
            <div class="select-wrapper">
              <select v-model="age" name="Age" id="age">
                <option v-for="age in ageOptions" v-bind:key="age" :value="age.id">{{age.value}}</option>
              </select>
            </div>
          </div>
          <div class="inputContainer">
            <label>Motion type</label>
            <div class="select-wrapper">
              <select v-model="type" name="Type" id="type">
                <option v-for="type in typeOptions" v-bind:key="type" :value="type.id">{{type.value}}</option>
              </select>
            </div>
          </div>
          <div class="inputContainer">
            <label>Training focus</label>
            <div class="select-wrapper">
              <select v-model="trainingFocus" name="trainingFocus" id="trainingFocus">
                  <option v-for="training in trainingOptions" v-bind:key="training" :value="training.id">{{training.value}}</option>
              </select>
            </div>
          </div>
          <div class="inputContainer">
            <label>Impro or prep</label>
          <div class="setting-container teams">
              <div class="radio-container">
                <span class="label">impro</span>
                <input
                  type="radio"
                  name="impro/prep"
                  v-model="improPrep"
                  :value="1"
                  >
              </div>
              <div class="radio-container">
                <span class="label">prep</span>
                <input
                  type="radio"
                  name="impro/prep"
                  v-model="improPrep"
                  :value="2"
                  >
              </div>
            </div>
          </div>
          <div class="inputContainer">
            <div class="subtitleContainer">
              <label>Add is used where</label><br/>
              <label class="subtitle"> Press Enter after each input</label>
            </div>
            <div class="arrayContainer" id="whereUsedContainer">
              <div class="linkContainer" v-for="(element, index) in usedWhere" :element="element.value" :key="element.value" :vid-id="index">
                  <span v-on:click="removeUsedWhere(index)"><img src="../assets/x.svg"/></span> {{element.value}}
              </div>
              <input type="text" id="used" key="used" placeholder="Type here..." @keydown.enter="addUsedWhere"/>
            </div>
          </div>
          <div class="inputContainer">
            <div class="subtitleContainer">
              <label>Add links</label><br/>
              <label class="subtitle">Press Enter after each input</label>
            </div>
            <div class="arrayContainer">
              <div class="linkContainer" v-for="(link, index) in links" :link="link" :key="link" :vid-id="index">
                <span v-on:click="removeLink(index)"><img src="../assets/x.svg"/></span> <a target="_blank" :href="link.value">{{link.text}}</a>
              </div>
              <input type="text" id="link" key="links.title" placeholder="Type name here..." />
              <input type="text" id="url" key="links.url" placeholder="Type url here..."/>
              <div class="buttonContainer">
                <p>Add another link</p>
                <button class="addLink btn" v-on:click="addLink"></button>
              </div>
            </div>
          </div>
          <button class="btn" type="submit">SUGGEST A MOTION</button>
        </form>
    </div>
  </div>
</div>
</template>

<script>
  export default {
    data() {
      return {
        categoryArray: [],
        chosenCategory: [],
        difficultiesArray: [],
        ageArray: [],
        debateFormatArray: [],
        typeArray: [],
        trainingFocusArray: [],
        improPrepArray: [],
        usedWhere: [],
        links: [],
        categories: 0,
        link: '',
        url: '',
        used: '',
        difficulty: 0,
        age: 0,
        debateFormat: 0,
        type: 0,
        trainingFocus: 0,
        improPrep: 0,
        isAuth: false
      }
    },
    methods: {
      addUsedWhere(event) {
        event.preventDefault()
        const width = document.getElementById('whereUsedContainer').offsetWidth;
        this.usedWhere.push({value: event.target.value})
        used.value = ''
      },
      removeUsedWhere(index) {
        this.usedWhere.splice(index, 1)
      },
      removeCategory(index) {
        this.chosenCategory.splice(index, 1)
      },
      addLink(event) {
        event.preventDefault()
        this.links.push({
          text: link.value,
          value: url.value
        })
        link.value = ''
        url.value = ''
      },
      removeLink(index) {
        this.links.splice(index, 1)
      },
      getOptions: (array) => {
        return Object.keys(array).map(key => {
          return array[key]
        })
      },
      postMotion: async function(e){
        e.preventDefault()
        try {
          await this.$store.dispatch('postMotion', {
            topic: this.$refs.topic.value,
            where_used: JSON.parse(JSON.stringify(this.usedWhere)),
            links: JSON.parse(JSON.stringify(this.links)),
            category: this.chosenCategory,
            difficulties: this.difficulty,
            age_range: this.age,
            debate_formats: this.debateFormat,
            type: this.type,
            training_focus: this.trainingFocus,
            impro_prep: this.improPrep
          })
          this.$router.push('/')
        } catch (error) {
          console.log('error: ', error);
        }
      }
    },
    computed:{
      categoryOptions() {
        const options = this.categoryArray.reduce((result, object) => {
            result[object.id] = object.value;
            return result;
        },{});
        return options;
      },
      difficultiesOptions() {
        return this.difficultiesArray;
      },
      ageOptions() {
        return this.ageArray;
      },
      debateFormatOptions() {
        return this.debateFormatArray;
      },
      typeOptions() {
        return this.typeArray;
      },
      trainingOptions() {
        return this.trainingFocusArray;
      },
      improPrepOptions() {
        return this.improPrepArray;
      }
    },
      watch: {
      // whenever question changes, this function will run
      categories: function (newValue, oldValue) {
          if (!this.chosenCategory.includes(newValue)) this.chosenCategory.push(newValue);
      }
    },
    async created() {
      this.isAuth = await this.$store.dispatch('isAuth')
      this.categoryArray = await this.$store.dispatch('getMotionAttributes', {type: 'categories'})
      this.difficultiesArray = await this.$store.dispatch('getMotionAttributes', {type: 'difficulties'})
      this.ageArray = await this.$store.dispatch('getMotionAttributes', {type: 'age-ranges'})
      this.debateFormatArray = await this.$store.dispatch('getMotionAttributes', {type: 'debate-formats'})
      this.typeArray = await this.$store.dispatch('getMotionAttributes', {type: 'types'})
      this.trainingFocusArray = await this.$store.dispatch('getMotionAttributes', {type: 'training-focuses'})
    }
  }
</script>

<style scoped lang="scss">

.container {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;

  .header {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #3098f3;
    padding-right: 30px;

    .logo {
      display: flex;
      align-items: center;

      span {
        font-family: Poppins;
        font-size: 18px;
        line-height: 29px;
        color: #252525;
        display: none;

        @media (min-width: 992px) {
          display: block;
        }
      }

      img {
        height: 30px;
        margin-left: 20px;

        @media (min-width: 768px) {
          height: 40px;
        }

        @media (min-width: 992px) {
          margin: 10px 10px 10px 40px;
          height: 74px;
        }

        @media (min-width: 1200px) {
          margin: 10px 10px 10px 100px;
        }
      }
    }

    .btn {
      color:white;

      @media (max-width: 575px) {
        padding: 5px 5px;
        font-size: 10px;
      }
    }
    .button {
      @media (max-width: 575px) {
        padding: 5px 5px;
        font-size: 10px;
      }
    }
  }

  .wrapper {
    width: 100%;

    @media (min-width: 768px) {
      width: 75%
    }

    @media (min-width: 1200px) {
      width: 50%
    }

    .motionSuggestContainer {
      display: flex;
      flex-direction: column;
      background-color: #ffffff;
      padding: 10px 20px;
      margin: 40px 10px;

      @media (min-width: 768px) {
        margin: 60px 10px 40px;
        padding: 20px 40px;
      }

      button[type="submit"] {
        margin-bottom: 20px;
      }
    }
  }
}

.textAreaContainer {
  position: relative;
  margin-bottom: 30px;

  textarea {
    display: block;
    resize: none;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
  }
}

.inputContainer {
  display: flex;
  border-top: 1px solid black;
  padding: 10px 0;
  flex-direction: column;

  @media (min-width: 576px) {
    flex-direction: row;
    justify-content: space-between;
  }

  & > label {
    @media (min-width: 576px) {
      line-height: 60px; //  must be same as input height
    }
  }

  .select-wrapper, .select-wrapper-full {
    width: 100%;
    cursor: pointer;
    position: relative;

    @media (min-width: 576px) {
      width: 50%;
    }

    select {
      width: 100%;
      -moz-appearance: none;
      -webkit-appearance: none;
      appearance: none;
      padding-right: 50px;
      cursor: pointer;
  }

    &:after {
      content: "";
      width: 25px;
      height: 25px;
      top: 10px;
      right: 10px;
      background-image: url("../assets/dropdown.svg");
      background-size: contain;
      position: absolute;
      pointer-events: none;

      @media (min-width: 768px) {
        width: 30px;
        height: 30px;
        top: 15px;
        right: 15px;
      }
    }
  }

  .arrayContainer {
    display: flex;
    flex-direction: column;
    font-family: Poppins;
    @media (min-width: 576px) {
      width: 50%;
    }
    img {
      width: 14px;
    }

    .select-wrapper-full {
      width: 100%;
      @media (min-width: 576px) {
        width: 100%;
      }
    }



    span {
      padding: 14px 28px 14px 0;
      font-size: 16px;
      display: inline-block;
      cursor: pointer;
    }

    input {
      margin-bottom: 10px;
      width: 100%
    }

    .linkContainer {
      text-overflow: ellipsis;
      white-space: nowrap;
      overflow: hidden;
    }

  }

  &:last-child {
    align-items: start;
  }

  .buttonContainer {
    display: flex;
    justify-content: flex-end;
    align-items: center;

    p {
      font-family: "IBM Plex Mono";
    }

    .addLink {
      background-image: url("../assets/plus.png");
      background-repeat: no-repeat;
      background-position: center;
      width: 42px;
      height: 42px;
      // border-radius: 21px;
      // background-color: #3098f3;
    }
  }
}

.radioContainer {
  display: flex;
  justify-content: space-evenly;
  width: 50%;
}

.subtitle {
  color: #252525;
  font-family: "IBM Plex Mono";
  font-size: 12px;
  font-style: italic;
  display: block;
  margin-top: -5px;

  @media (min-width: 768px) {
    font-size: 14px;
    line-height: 16px;
  }
}

.line {
  margin-top: 26px;
  border-top: 1px solid;
}

.setting-container {
  width: 50%;

  @media (min-width: 768px) {
    display: flex;
    justify-content: start;

  }

  .radio-container {
    padding-left: 2px;
    font-family: Poppins;
    font-size: 16px;
    line-height: 48px;
    display: block;
    float: left;
    overflow: hidden;
    @media (min-width: 768px) {
      font-size: 20px;
      line-height: 60px;
    }
    span {
      display: block;
      float: right;
      padding-left: 10px;
      width: auto;
    }
    &:nth-child(1) {
      margin-right: 20%;
      @media (min-width: 768px) {
        margin-right: 20%;
      }
    }
    input[type="radio"] {
      width: 30px;
      line-height: 60px;
      display: inline-block;
      top: 12px;
      @media (min-width: 768px) {
        top: 17px;
      }
    }
  }

  @supports(-webkit-appearance: none) or (-moz-appearance: none) {
    input[type='radio'] {
      --active: #ffffff;
      --active-inner: #3098f3;
      --focus: 2px rgba(39, 94, 254, .3);
      --border: #3098f3;
      --border-hover: #3098f3;
      --background: #fff;
      --disabled: #F6F8FF;
      --disabled-inner: #E1E6F9;
      -webkit-appearance: none;
      -moz-appearance: none;
      height: 25px;
      outline: none;
      display: inline-block;
      vertical-align: top;
      position: relative;
      margin: 0;
      cursor: pointer;
      // border: 4px solid var(--bc, var(--border));
      border: 3px solid #3098f3;
      border-radius: 50%;
      background: var(--b, var(--background));
      transition: background .3s, border-color .3s, box-shadow .2s;
      &:after {
        content: '';
        display: block;
        left: 0;
        top: 0;
        position: absolute;
        transition: transform var(--d-t, .3s) var(--d-t-e, ease), opacity var(--d-o, .2s);
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: var(--active-inner);
        opacity: 0;
        transform: scale(var(--s, .7));
      }
      &:checked {
        --b: var(--active);
        --bc: var(--active);
        --d-o: .3s;
        --d-t: .6s;
        --d-t-e: cubic-bezier(.2, .85, .32, 1.2);
      }
      &:disabled {
        --b: var(--disabled);
        cursor: not-allowed;
        opacity: .9;
        &:checked {
          // --b: var(--disabled-inner);
          // --bc: var(--border);
        }
        &+label {
          cursor: not-allowed;
        }
      }
      &:hover {
        &:not(:checked) {
          &:not(:disabled) {
            --bc: var(--border-hover);
          }
        }
      }
      &:focus {
        box-shadow: 0 0 0 var(--focus);
      }
      &:not(.switch) {
        width: 25px;
        &:after {
          opacity: var(--o, 0);
        }
        &:checked {
          --o: 1;
        }
      }
      &+label {
        font-size: 14px;
        line-height: 25px;
        display: inline-block;
        vertical-align: top;
        cursor: pointer;
        margin-left: 4px;
      }
    }

    input[type='checkbox'] {
      &:not(.switch) {
        border-radius: 7px;
        &:after {
          width: 5px;
          height: 9px;
          border: 2px solid var(--active-inner);
          border-top: 0;
          border-left: 0;
          left: 7px;
          top: 4px;
          transform: rotate(var(--r, 20deg));
        }
        &:checked {
          --r: 43deg;
        }
      }
      &.switch {
        width: 38px;
        border-radius: 11px;
        &:after {
          left: 2px;
          top: 2px;
          border-radius: 50%;
          width: 15px;
          height: 15px;
          background: var(--ab, var(--border));
          transform: translateX(var(--x, 0));
        }
        &:checked {
          --ab: var(--active-inner);
          --x: 17px;
        }
        &:disabled {
          &:not(:checked) {
            &:after {
              opacity: .6;
            }
          }
        }
      }
    }
  }
}

</style>
