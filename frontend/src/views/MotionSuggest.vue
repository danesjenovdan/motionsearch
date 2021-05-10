<template>
  <div class="background">
      <div class="grandParentContaniner">
          <div class="motionSuggestContainer">
            <h1>Suggest a motion</h1><br>
           <form @submit="postMotion">
              <div class="textAreaContainer">
                <label>Topic</label><br>
                <textarea rows="3" cols="20" name="topic" id="topic"></textarea>
               </div><br>
              <div class="inputContainer"> 
                <label >Category</label>
                <select v-model="categories" name="Category" id="categories">
                  <option v-for="category in categoryOptions" v-bind:key="category" :value="category.id">{{category.value}}</option>
                </select>
              </div>
              <div class="inputContainer"> 
                <label>Dificulty</label>
                <select v-model="difficulty" name="Dificulty" id="difficulty">
                  <option v-for="difficulty in difficultiesOptions" v-bind:key="difficulty" :value="difficulty.id">{{difficulty.value}}</option>
                </select>
              </div>
              <div class="inputContainer"> 
                <label>Debate format</label>
                <select v-model="debateFormat" name="DebateFormat" id="debateFormat">
                  <option v-for="debateFormat in debateFormatOptions" v-bind:key="debateFormat" :value="debateFormat.id">{{debateFormat.value}}</option>
                </select>
              </div>
              <div class="inputContainer"> 
                <label >Age</label>
                <select v-model="age" name="Age" id="age">
                  <option v-for="age in ageOptions" v-bind:key="age" :value="age.id">{{age.value}}</option>
                </select>
              </div>
              <div class="inputContainer"> 
                <label>Motion type</label>
                <select v-model="type" name="motionType" id="motionType">
                  <option v-for="type in typeOptions" v-bind:key="type" :value="type.id">{{type.value}}</option>
                </select>
              </div>
              <div class="inputContainer"> 
                <label>Training focus</label>
                <select v-model="trainingFocus" name="trainingFocus" id="trainingFocus">
                    <option v-for="training in trainingOptions" v-bind:key="training" :value="training.id">{{training.value}}</option>
                </select>
              </div>
              <div class="inputContainer"> 
                <label>Impro or prep</label>
              <div class="setting-container teams">
                  <div class="radio-container">
                    <span class="label">impro</span>
                    <input
                      type="radio"
                      name="impro/prep"
                      :value="1"
                      >
                  </div>
                  <div class="radio-container">
                    <span class="label">prep</span>
                    <input
                      type="radio"
                      name="impro/prep"
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
                <div class="arrayContainer">
                  <div v-for="(element, index) in usedWhere" :element="element" :key="element" :vid-id="index">
                     <button v-on:click="removeUsedWhere(index)" class="btn">x</button> {{element}}
                  </div>
                  <input type="text" key="used" placeholder="Type here..." @keydown.enter="addUsedWhere"/>
                </div>
              </div>
              <div class="inputContainer"> 
                <div class="subtitleContainer">
                  <label>Add links</label><br/>
                  <label class="subtitle"> Press Enter after each input</label>
                </div>
                <div class="arrayContainer">
                  <div v-for="(link, index) in links" :link="link" :key="link" :vid-id="index">
                    <button v-on:click="removeLink(index)" class="btn">x</button> <a target="_blank" :href="link.url">{{link.title}}</a>
                  </div>
                  <input type="text" id="link" key="links.title" placeholder="Type here..." />
                  <input type="text" id="url" key="links.url" placeholder="Type here..."/>
                  <button v-on:click="addLink">Add link</button>
                </div>
              </div>
              <button type="submit">Submit motion</button>
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
        difficultiesArray: [],
        ageArray: [],
        debateFormatArray: [],
        typeArray: [],
        trainingFocusArray: [],
        improPrepArray: [],
        usedWhere: [],
        links: [],
        topic: '',
        categories: 0,
        link: '',
        url: '',
        difficulty: 0,
        age: 0,
        debateFormat: 0,
        motionType: 0,
        trainingFocus: 0,
        improPrep: 0
      }
    },
    methods: {
      addUsedWhere(event) {
        event.preventDefault()
        this.usedWhere.push(event.target.value)
      },
      removeUsedWhere: (index) => {
        event.preventDefault()
        this.usedWhere.splice(index, 1)
      },
      addLink(event) {
        event.preventDefault()
        this.links.push({
          title: link.value,
          url: url.value
        })
        link.value = ''
        url.value = ''
      },
      removeLink(index) {
        event.preventDefault()
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
            topic: this.topic,
            where_used: JSON.parse(JSON.stringify(this.usedWhere)),
            links: JSON.parse(JSON.stringify(this.links)),
            category: this.categories,
            difficulty: this.difficulty,
            age_range: this.age,
            debate_formats: this.debateFormat,
            type: this.motionType,
            training_focus: this.trainingFocus,
            impro_prep: this.improPrep
          })
          window.location.href = '/';
        } catch (error) {
          console.log('error: ', error);
        }
      }
    },
    computed:{
      categoryOptions() {
        return this.categoryArray;
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
      },
      debateFormatOptions() {
        return this.debateFormatArray;
      }
    },
    async created() {
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

	.grandParentContaniner{
	  display:flex;
    margin: 0 auto; ;
    justify-content: center;
    align-items: center;
	}
  
  .inputContainer {
    display: flex;
    border-top: 1px solid black;
    padding: 10px;
    justify-content: space-between;
  }
  .arrayContainer {
    display: flex;
    flex-direction: column;
    width: 50%;
  }
  .radioContainer {
    display: flex;
    justify-content: space-evenly;
    width: 50%;
  }
  .subtitle {
    color: #252525;
    font-family: "IBM Plex Mono";
    font-size: 14px;
    font-style: italic;
    letter-spacing: normal;
    margin-top: -50px;
    text-align: left;
  }
  .btn {
    border: none;
    background-color: inherit;
    padding: 14px 28px;
    font-size: 16px;
    cursor: pointer;
    display: inline-block;
    color: black;
  }
  .textAreaContainer{
    position: relative;
    margin-bottom: 20px;
  }
   textarea {
    display: block;
    resize: none;
    width: 100%;
    height: 100%; 
    box-sizing: border-box;
  }
  .background {
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%), linear-gradient(to top, #000000 0%, #ffffff 100%);
  }
  .motionSuggestContainer {
      display: flex;
      flex-direction: column;
      background-color: #ffffff;
      width: 50vw;
      padding: 40px;
      margin-top: 100px;
      margin-bottom: 40px;
  }
  .line {
    margin-top: 26px;
    border-top: 1px solid;
  }
  .login-text {
    display: flex;
    justify-content: center;
  }
  input {
      box-sizing: border-box;
  }
  select {
    width: 50%;
    height: 60px;
  }
  .setting-container {
    display: flex;
    justify-content: start;
    align-items: left;
    width: 50%;

  .radio-container {
    padding-left: 2px;
    font-family: Poppins;
    font-size: 20px;
    font-weight: 400;
    line-height: 60px;
    display: block;
    float: left;
    overflow: hidden;
    margin-top: 14px;
    span {
      display: block;
      float: right;
      padding-left: 10px;
      width: auto;
    }
    &:nth-child(1) {
      margin-right: 20%;
    }
    input[type="radio"] {
      width: 30px;
      line-height: 60px;
      display: inline-block;
      &:nth-child(1) {
        top: 17px;
      }
      &:nth-child(2) {
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
      background: var(--b, var(--background));
      transition: background .3s, border-color .3s, box-shadow .2s;
      &:after {
        content: '';
        display: block;
        left: 0;
        top: 0;
        position: absolute;
        transition: transform var(--d-t, .3s) var(--d-t-e, ease), opacity var(--d-o, .2s);
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
    input[type='radio'] {
      border-radius: 50%;
      &:after {
        width: 19px;
        height: 19px;
        border-radius: 50%;
        background: var(--active-inner);
        opacity: 0;
        transform: scale(var(--s, .7));
      }
      // &:checked {
      //   --s: .5;
      // }
    }
  }
  }



</style>