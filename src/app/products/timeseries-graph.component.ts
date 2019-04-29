import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { IProduct } from './product';
import { ProductService } from './product.service';

@Component({
  templateUrl: './timeseries-graph.component.html',
  styleUrls: ['./timeseries-graph.component.css']
})
export class TimeseriesGraphComponent implements OnInit {

  pageTitle = 'Timeseries Graphs!';
  page: any;
  sub: any;
  index: number;
  constructor(private router: Router, private route: ActivatedRoute) { }

  ngOnInit() {
    this.sub = this.route
    .queryParams
    .subscribe(params => {
      // Defaults to 0 if no query param provided.
      this.page = +params['page'] || 0;
      this.index = this.page;
      console.log(this.page);
    });
  }
  onBack(): void {
    this.router.navigate(['/timeseries']);
  }

}
