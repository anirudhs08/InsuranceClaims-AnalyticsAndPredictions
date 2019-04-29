import { Component } from '@angular/core';

@Component({
  selector: 'pm-root',
  template: `
  <style>
    body { height:100%; }
  </style>
  <body><!-- style="background-color:black;">-->
    <nav class='navbar navbar-expand navbar-light bg-light'>
        <a class='navbar-brand'>{{pageTitle}}</a>
        <ul class='nav nav-pills'>
          <li><a class='nav-link' routerLinkActive='active' [routerLink]="['/welcome']">Home</a></li>
          <li><a class='nav-link' routerLinkActive='active' [routerLink]="['/products']">Algorithms List</a></li>
          <li><a class='nav-link' routerLinkActive='active' [routerLink]="['/timeseries']">Time Series</a></li>
          <li><a class='nav-link' routerLinkActive='active' [routerLink]="['/customerDetails']">Customer Details</a></li>
          
        </ul>
    </nav>
    <div class='container'>
      <router-outlet></router-outlet>
    </div>
    </body>
    `,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  pageTitle = 'Vantage Agora';
}
