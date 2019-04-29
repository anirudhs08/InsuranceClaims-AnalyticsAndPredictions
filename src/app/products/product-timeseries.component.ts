import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, NavigationExtras } from '@angular/router';

import { IProduct } from './product';
import { ProductService } from './product.service';

@Component({
  templateUrl: './product-timeseries.component.html',
  styleUrls: ['./product-timeseries.component.css']
})
export class ProductTimeseriesComponent implements OnInit {
  pageTitle = 'Time-Series';
  pageNum: number;
 
  
  constructor(private router: Router,) { }

  ngOnInit() {
  }

  checkedBoxA(event): void {
    
    if(event.target.checked)
    {
      console.log(event.srcElement.defaultValue);
      this.pageNum = event.srcElement.defaultValue;
      this.router.navigate(['/timeseriesGraph'], { queryParams: { page: this.pageNum } }  );   
      
    }
    
  }
}
