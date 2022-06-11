<template>
    <v-app>

<!-- <v-system-bar app height="30" color="primary">The system bar</v-system-bar> -->

<v-app-bar app color="secondary" height="70" dense dark clipped-left>
  The application bar
</v-app-bar>

<v-navigation-drawer app  clipped>
  <p>Navigation drawer</p>
</v-navigation-drawer>

<v-main>
  <v-container>
    <router-view></router-view>
  </v-container>
</v-main>

<v-footer app>The footer</v-footer>
<v-bottom-navigation app color="secondary">The bottom navigation</v-bottom-navigation>
</v-app>
</template>
