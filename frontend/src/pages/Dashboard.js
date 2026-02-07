import React from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
  const stats = [
    { label: '酒柜物品', value: '12', change: '+2', link: '/bar-items' },
    { label: '可用配方', value: '8', change: '+3', link: '/recipes' },
    { label: '调酒记录', value: '5', change: '+1', link: '/cocktail-records' },
    { label: '待购物品', value: '4', change: '-1', link: '/shopping-list' },
  ];

  const recentActivities = [
    { id: 1, action: '添加了配方', target: '莫吉托', time: '2小时前' },
    { id: 2, action: '记录了调酒', target: '古典鸡尾酒', time: '1天前' },
    { id: 3, action: '更新了库存', target: '金酒剩余 200ml', time: '2天前' },
    { id: 4, action: '购买了', target: '柠檬 × 5', time: '3天前' },
  ];

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">欢迎回来！</h1>
        <p className="text-gray-600 mt-2">今天想尝试什么新配方？</p>
      </div>

      {/* 统计卡片 */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {stats.map((stat) => (
          <Link
            key={stat.label}
            to={stat.link}
            className="card hover:shadow-lg transition-shadow"
          >
            <div className="flex justify-between items-start">
              <div>
                <p className="text-gray-600 text-sm">{stat.label}</p>
                <p className="text-3xl font-bold mt-2">{stat.value}</p>
              </div>
              <span className="text-sm px-2 py-1 rounded-full bg-green-100 text-green-800">
                {stat.change}
              </span>
            </div>
          </Link>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* 快速操作 */}
        <div className="card">
          <h2 className="text-xl font-bold mb-4">快速操作</h2>
          <div className="space-y-4">
            <Link
              to="/recipes?filter=available"
              className="flex items-center p-4 border rounded-lg hover:bg-gray-50 transition-colors"
            >
              <div className="p-2 bg-primary-100 rounded-lg mr-4">
                <svg className="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <h3 className="font-medium">查看可制作配方</h3>
                <p className="text-sm text-gray-600">根据现有材料筛选</p>
              </div>
            </Link>
            
            <Link
              to="/bar-items?action=add"
              className="flex items-center p-4 border rounded-lg hover:bg-gray-50 transition-colors"
            >
              <div className="p-2 bg-green-100 rounded-lg mr-4">
                <svg className="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
              </div>
              <div>
                <h3 className="font-medium">添加新物品到酒柜</h3>
                <p className="text-sm text-gray-600">记录新购买的基酒或材料</p>
              </div>
            </Link>
            
            <Link
              to="/recipes?action=add"
              className="flex items-center p-4 border rounded-lg hover:bg-gray-50 transition-colors"
            >
              <div className="p-2 bg-blue-100 rounded-lg mr-4">
                <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <div>
                <h3 className="font-medium">添加新配方</h3>
                <p className="text-sm text-gray-600">记录从各处收集的配方</p>
              </div>
            </Link>
          </div>
        </div>

        {/* 最近活动 */}
        <div className="card">
          <h2 className="text-xl font-bold mb-4">最近活动</h2>
          <div className="space-y-4">
            {recentActivities.map((activity) => (
              <div key={activity.id} className="flex items-center p-3 border rounded-lg">
                <div className="flex-1">
                  <p className="font-medium">
                    <span className="text-gray-700">{activity.action}</span>{' '}
                    <span className="text-primary-600">{activity.target}</span>
                  </p>
                  <p className="text-sm text-gray-500">{activity.time}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;