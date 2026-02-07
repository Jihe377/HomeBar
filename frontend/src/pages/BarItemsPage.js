import React, { useState } from 'react';
import BarItemCard from '../components/BarItemCard';
import BarItemForm from '../components/BarItemForm';

const BarItemsPage = () => {
  const [showForm, setShowForm] = useState(false);
  
  // 模拟数据
  const barItems = [
    { id: 1, name: '金酒', category: 'spirit', brand: 'Gordon\'s', volume: 750, currentVolume: 500, abv: 40, isAvailable: true },
    { id: 2, name: '柠檬汁', category: 'fruit', brand: '鲜榨', volume: 500, currentVolume: 200, abv: 0, isAvailable: true },
    { id: 3, name: '糖浆', category: 'other', brand: '自制', volume: 250, currentVolume: 100, abv: 0, isAvailable: true },
    { id: 4, name: '苏打水', category: 'mixer', brand: '屈臣氏', volume: 330, currentVolume: 330, abv: 0, isAvailable: true },
    { id: 5, name: '朗姆酒', category: 'spirit', brand: 'Bacardi', volume: 750, currentVolume: 0, abv: 40, isAvailable: false },
  ];

  const categories = [
    { value: 'spirit', label: '基酒', color: 'bg-red-100 text-red-800' },
    { value: 'liqueur', label: '利口酒', color: 'bg-purple-100 text-purple-800' },
    { value: 'wine', label: '葡萄酒', color: 'bg-pink-100 text-pink-800' },
    { value: 'beer', label: '啤酒', color: 'bg-amber-100 text-amber-800' },
    { value: 'mixer', label: '调酒饮料', color: 'bg-blue-100 text-blue-800' },
    { value: 'fruit', label: '水果', color: 'bg-green-100 text-green-800' },
    { value: 'herb', label: '香草', color: 'bg-emerald-100 text-emerald-800' },
    { value: 'other', label: '其他', color: 'bg-gray-100 text-gray-800' },
  ];

  const handleAddItem = (itemData) => {
    console.log('添加物品:', itemData);
    setShowForm(false);
    // 这里应该调用API
  };

  const handleEditItem = (itemId) => {
    console.log('编辑物品:', itemId);
    // 这里应该打开编辑表单
  };

  const handleDeleteItem = (itemId) => {
    console.log('删除物品:', itemId);
    // 这里应该调用API
  };

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">我的酒柜</h1>
          <p className="text-gray-600 mt-2">管理您的基酒、材料和库存</p>
        </div>
        <button
          onClick={() => setShowForm(true)}
          className="btn-primary flex items-center"
        >
          <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          添加物品
        </button>
      </div>

      {/* 分类筛选 */}
      <div className="mb-6">
        <div className="flex flex-wrap gap-2">
          <button className="px-4 py-2 bg-primary-600 text-white rounded-lg">
            全部
          </button>
          {categories.map((cat) => (
            <button
              key={cat.value}
              className={`px-4 py-2 rounded-lg ${cat.color}`}
            >
              {cat.label}
            </button>
          ))}
        </div>
      </div>

      {/* 物品列表 */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {barItems.map((item) => (
          <BarItemCard
            key={item.id}
            item={item}
            onEdit={handleEditItem}
            onDelete={handleDeleteItem}
          />
        ))}
      </div>

      {/* 添加表单模态框 */}
      {showForm && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg w-full max-w-2xl max-h-[90vh] overflow-y-auto">
            <div className="p-6">
              <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-bold">添加新物品</h2>
                <button
                  onClick={() => setShowForm(false)}
                  className="text-gray-500 hover:text-gray-700"
                >
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
              <BarItemForm onSubmit={handleAddItem} onCancel={() => setShowForm(false)} />
            </div>
          </div>
        </div>
      )}

      {barItems.length === 0 && (
        <div className="text-center py-12">
          <svg className="w-16 h-16 mx-auto text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
          </svg>
          <h3 className="mt-4 text-lg font-medium text-gray-900">酒柜空空如也</h3>
          <p className="mt-2 text-gray-600">添加您的第一件物品来开始吧！</p>
          <button
            onClick={() => setShowForm(true)}
            className="mt-4 btn-primary"
          >
            添加物品
          </button>
        </div>
      )}
    </div>
  );
};

export default BarItemsPage;