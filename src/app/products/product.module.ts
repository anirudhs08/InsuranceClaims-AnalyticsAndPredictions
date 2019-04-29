import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

import { ProductListComponent } from './product-list.component';
import { ProductDetailComponent } from './product-detail.component';
import { ConvertToSpacesPipe } from '../shared/convert-to-spaces.pipe';
import { ProductDetailGuard } from './product-detail.guard';
import { SharedModule } from '../shared/shared.module';
import { ProductTimeseriesComponent } from './product-timeseries.component';
import { TimeseriesGraphComponent } from './timeseries-graph.component';
import { CustomerDetailsComponent } from './customer-details.component';
import { TestPageComponent } from './test-page.component';

@NgModule({
  imports: [
    RouterModule.forChild([
      { path: 'products', component: ProductListComponent },
      {
        path: 'products/:id',
        canActivate: [ProductDetailGuard],
        component: ProductDetailComponent
      },
      { path: 'timeseries', component: ProductTimeseriesComponent },
      { path: 'timeseriesGraph', component: TimeseriesGraphComponent },
      { path: 'customerDetails', component: CustomerDetailsComponent },
      { path: 'testPage', component: TestPageComponent },
      //{ path: 'timeseries', component: ProductTimeseriesComponent },

    ]),
    SharedModule
  ],
  declarations: [
    ProductListComponent,
    ProductDetailComponent,
    ConvertToSpacesPipe,
    ProductTimeseriesComponent,
    TimeseriesGraphComponent,
    CustomerDetailsComponent,
    TestPageComponent
  ]
})
export class ProductModule { }
