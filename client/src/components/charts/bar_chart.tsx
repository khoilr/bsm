import * as echarts from 'echarts';

import EchartReact from 'echarts-for-react';

// option && myChart.setOption(option);
function BarChart() {
    var app: any = {};
    type EChartsOption = echarts.EChartsOption;

    var chartDom = document.getElementById('main')!;

    let option: EChartsOption;

    const posList = [
        'left',
        'right',
        'top',
        'bottom',
        'inside',
        'insideTop',
        'insideLeft',
        'insideRight',
        'insideBottom',
        'insideTopLeft',
        'insideTopRight',
        'insideBottomLeft',
        'insideBottomRight'
    ] as const;


    type BarLabelOption = NonNullable<echarts.BarSeriesOption['label']>;

    // const labelOption: BarLabelOption = {
    //     show: true,
    //     position: app.config.position as BarLabelOption['position'],
    //     distance: app.config.distance as BarLabelOption['distance'],
    //     align: app.config.align as BarLabelOption['align'],
    //     verticalAlign: app.config.verticalAlign as BarLabelOption['verticalAlign'],
    //     rotate: app.config.rotate as BarLabelOption['rotate'],
    //     formatter: '{c}  {name|{a}}',
    //     fontSize: 16,
    //     rich: {
    //         name: {}
    //     }
    // };

    option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['Forest', 'Steppe', 'Desert', 'Wetland']
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: { show: true },
                dataView: { show: true, readOnly: false },
                magicType: { show: true, type: ['line', 'bar', 'stack'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: { show: false },
                data: ['2012', '2013', '2014', '2015', '2016']
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: 'Forest',
                type: 'bar',
                barGap: 0,
                // label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [320, 332, 301, 334, 390]
            },
            {
                name: 'Steppe',
                type: 'bar',
                // label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [220, 182, 191, 234, 290]
            },
            {
                name: 'Desert',
                type: 'bar',
                // label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [150, 232, 201, 154, 190]
            },
            {
                name: 'Wetland',
                type: 'bar',
                // label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [98, 77, 101, 99, 40]
            }
        ]
    };

    return (
        <div className='w-full'>
            <EchartReact className='w-full' option={option} style={{ height: 800 }} />
        </div>

    )
}

export default BarChart;