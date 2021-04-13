<template>
  <div class="container">
    <div @click="toggleSelectedUp" :class="{ 'upvote-button': upSelected, 'upvote-button-unselected': !upSelected }"/>
    <span class="upvotes-number">{{number}}</span>
    <div @click="toggleSelectedDown" :class="{ 'downvote-button': downSelected, 'downvote-button-unselected': !downSelected }"/>
  </div>
</template>

<script>
export default {
  data() {
    return{
      upSelected: false,
      downSelected: false,
      number: Math.floor(Math.random() * 100),
    }
  }, 
  methods: {
    toggleSelectedUp: function () {
      this.upSelected = !this.upSelected;
      if(this.downSelected) { 
        this.downSelected = !this.downSelected;
        this.number += 1;  
      }
      this.number = this.upSelected ? this.number+1 : this.number-1
    },
    toggleSelectedDown: function () {
      this.downSelected = !this.downSelected;
      if(this.upSelected) { 
        this.upSelected = !this.upSelected;
        this.number -= 1;
        }
      this.number = this.downSelected ? this.number-1 : this.number+1
    }
  }
}
</script>

<style scoped lang="scss">
  .upvote-button {
    background-image: url('../assets/up-selected.png');
    width: 100px;
    height: 100px;
    background-position: center;
    background-repeat: no-repeat;
    cursor:pointer;
  }
  .upvote-button-unselected {
    background-image: url('../assets/up-unselected.png');
    width: 100px;
    height: 100px;
    background-position: center;
    background-repeat: no-repeat;
    cursor:pointer;
  }
  .downvote-button {
    background-image: url('../assets/down-selected.png');
    width: 100px;
    height: 100px;
    background-position: center;
    background-repeat: no-repeat;
    cursor:pointer;
  }
  .downvote-button-unselected {
    background-image: url('../assets/down-unselected.png');
    width: 100px;
    height: 100px;
    background-position: center;
    background-repeat: no-repeat;
    cursor:pointer;
  }

  .container {
    display: flex;
    flex-direction: column;
    width: 75px;
    height: 75px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-right: 20px;
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%);
  }
  img {
    cursor: pointer;
  }
  .upvotes-number {
    color: #252525;
    font-family: Poppins;
    font-size: 18px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    text-align: center;
  }
</style>