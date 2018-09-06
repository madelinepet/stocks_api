from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import numpy as np
import pandas as pd
import bokeh.plotting as bk
# hover pan, zoom, reset, lables, etc tools
from bokeh.models import HoverTool, Label, BoxZoomTool, PanTool, ZoomInTool, ZoomOutTool, ResetTool
import requests
from urllib.parse import urlparse

API_URL = 'https://api.iextrading.com/1.0'


class VisualizationAPIViewset(APIViewSet):
    def retrieve(self, request, id=None):
        """ Gets the chart and saves as an html file when this route is hit
        """
        parsed_url = request.current_route_url()
        chart_type = urlparse(parsed_url).query.split('=')[1]

        if chart_type == 'candlestick':
            res = requests.get(f'{API_URL}/stock/{id}/chart/5y')
            data = res.json()
            df = pd.DataFrame(data)
            seqs = np.arange(df.shape[0])
            df['seqs'] = pd.Series(seqs)
            df['changePercent'] = df['changePercent'].apply(lambda x: str(x) + '%')
            # axis of one means go down the comumns, not the whole row. Default of 0 operates on the rows.
            df['mid'] = df.apply(lambda x: (x['open'] + x['close'])/2, axis=1)
            df.head(1)
            df['height'] = df.apply(
                lambda x: x['close'] - x['open'] if x['close'] != x['open'] else 0.001,
                axis=1
            )
            df.sample(2)
            inc = df.close > df.open
            dec = df.close < df.open
            w = .3
            sourceInc = bk.ColumnDataSource(df.loc[inc])
            sourceDec = bk.ColumnDataSource(df.loc[dec])
            hover = HoverTool(
                tooltips=[
                    ('date', '@date'),
                    ('low', '@low'),
                    ('high', '@high'),
                    ('open', '@open'),
                    ('close', '@close'),
                    ('percent', '@percent'),
                    ]
            )
            TOOLS = [hover, BoxZoomTool(), PanTool(), ZoomInTool(), ZoomOutTool(), ResetTool()]
            p = bk.figure(plot_width=1500, plot_height=800, tools=TOOLS, title=f'{id.upper()}', toolbar_location='above')
            p.xaxis.major_label_orientation = np.pi/4
            p.grid.grid_line_alpha = w
            descriptor = Label(x=70, y=70, text='Label goes here')
            # adds label onto the chart
            p.add_layout(descriptor)
            # set up your outer tails, and then the rectangles that go inside of the tails
            p.segment(df.seqs[inc], df.high[inc], df.seqs[inc], df.low[inc], color='green')
            p.segment(df.seqs[dec], df.high[dec], df.seqs[dec], df.low[dec], color='red')
            p.rect(x='seqs', y='mid', width=w, height='height', fill_color='green', line_color='green', source=sourceInc)
            p.rect(x='seqs', y='mid', width=w, height='height', fill_color='red', line_color='red', source=sourceDec)
            bk.save(
                p,
                f'./stocks_api_project/static/candle_stick_{id}.html',
                title=f'5yr_candlestick_{id}'
            )

        if chart_type == 'bar':
            res = requests.get(f'{API_URL}/stock/{id}/chart/5y')
            data = res.json()
            df = pd.DataFrame(data)
            df['date'] = pd.to_datetime(df['date'])
            df['MONTH'] = df['date'].dt.month
            df['DAY'] = df['date'].dt.day
            df['YEAR'] = df['date'].dt.year
            df[['low']].groupby(df.YEAR).mean()
            plot = bk.figure(
                    plot_width=400,
                    plot_height=400
                )
            plot.vbar(
                x=df.YEAR,
                width=0.5,
                bottom=0,
                top=df.low,
                color="firebrick"
            )

            bk.save(
                plot,
                f'./stocks_api_project/static/year_versus_low_{id}.html',
                title=f'5yr_low_bar_{id}'
            )

        if chart_type == 'volatility':
            res = requests.get(f'{API_URL}/stock/{id}/chart/5y')
            data = res.json()
            df = pd.DataFrame(data)
            df['date'] = pd.to_datetime(df['date'])
            df['MONTH'] = df['date'].dt.month
            df['DAY'] = df['date'].dt.day
            df['YEAR'] = df['date'].dt.year
            df[['change']].groupby(df.DAY).mean()
            plot_2 = bk.figure(
                plot_width=400,
                plot_height=400
            )
            plot_2.vbar(
                x=df.DAY,
                width=0.5,
                bottom=0,
                top=df.change,
                color="blue"
            )

            bk.save(
                plot_2,
                f'./stocks_api_project/static/volatility_{id}.html',
                title=f'5yr_volitility_bar_{id}'
            )

        return Response(json={'message': 'Listing the chart'}, status=200)
