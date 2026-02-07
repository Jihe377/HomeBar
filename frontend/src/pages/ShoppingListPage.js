import React, { useState } from 'react';

const ShoppingListPage = () => {
  const [items, setItems] = useState([
    { id: 1, name: '金酒', quantity: 1, unit: '瓶', priority: 1, purchased: false },
    { id: 2, name: '柠檬', quantity: 5, unit: '个', priority: 2, purchased: false },
    { id: 3, name: '糖浆', quantity: 1, unit: '瓶', priority: 3, purchased: true },
    { id: 4, name: '苏打水', quantity: 6, unit: '罐', priority: 2, purchased: false },
  ]);

  const handleTogglePurchase = (id) => {
    setItems(items.map(item => 
      item.id === id ? { ...item, purchased: !item.purchased } : item
    ));
  };

  const handleDelete = (id) => {
    setItems(items.filter(item => item.id !== id));
  };

  const handleAddItem = () => {
    const newItem = {
      id: items.length + 1,
      name: '',
      quantity: 1,
      unit: '个',
      priority: 3,
      purchased: false,
    };
    setItems([...items, newItem]);
  };

  const getPriorityColor = (priority) => {
    const colors = {
      1: 'bg-red-100 text-red-800',
      2: 'bg-yellow-100 text-yellow-800',
      3: 'bg-blue-100 text-blue-800',
      4: 'bg-gray-100 text-gray-800',
      5: 'bg-gray-100 text-gray-800',
    };
    return colors[priority] || colors[3];
  };

  const getPriorityLabel = (priority) => {
    const labels = {
      1: '高',
      2: '中',
      3: '低',
      4: '极低',
      5: '极低',
    };
    return labels[priority] || '低';
  };

  const pendingItems = items.filter(item => !item.purchased);
  const purchasedItems = items.filter(item => item.purchased);

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">购物清单</h1>
          <p className="text-gray-600 mt-2">管理您需要购买的调酒材料</p>
        </div>
        <button
          onClick={handleAddItem}
          className="btn-primary flex items-center"
        >
          <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          添加物品
        </button>
      </div>

      {/* 待购物品 */}
      <div className="card mb-8">
        <h2 className="text-xl font-bold mb-4">待购物品 ({pendingItems.length})</h2>
        {pendingItems.length > 0 ? (
          <div className="space-y-3">
            {pendingItems.map((item) => (
              <div key={item.id} className="flex items-center justify-between p-3 border rounded-lg">
                <div className="flex items-center">
                  <button
                    onClick={() => handleTogglePurchase(item.id)}
                    className="w-5 h-5 border rounded mr-3 flex items-center justify-center"
                  >
                    {item.purchased && (
                      <svg className="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                    )}
                  </button>
                  <div>
                    <h3 className="font-medium">{item.name}</h3>
                    <p className="text-sm text-gray-600">{item.quantity} {item.unit}</p>
                  </div>
                </div>
                <div className="flex items-center space-x-2">
                  <span className={`px-3 py-1 rounded-full text-xs font-medium ${getPriorityColor(item.priority)}`}>
                    {getPriorityLabel(item.priority)}优先级
                  </span>
                  <button
                    onClick={() => handleDelete(item.id)}
                    className="text-red-600 hover:text-red-900"
                  >
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-8">
            <svg className="w-12 h-12 mx-auto text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <h3 className="mt-4 text-lg font-medium text-gray-900">购物清单已完成！</h3>
            <p className="mt-2 text-gray-600">所有物品都已购买</p>
          </div>
        )}
      </div>

      {/* 已购物品 */}
      {purchasedItems.length > 0 && (
        <div className="card">
          <h2 className="text-xl font-bold mb-4">已购物品 ({purchasedItems.length})</h2>
          <div className="space-y-3">
            {purchasedItems.map((item) => (
              <div key={item.id} className="flex items-center justify-between p-3 border rounded-lg bg-gray-50">
                <div className="flex items-center">
                  <div className="w-5 h-5 border rounded mr-3 flex items-center justify-center bg-green-100 border-green-300">
                    <svg className="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <div>
                    <h3 className="font-medium line-through text-gray-500">{item.name}</h3>
                    <p className="text-sm text-gray-500">{item.quantity} {item.unit}</p>
                  </div>
                </div>
                <button
                  onClick={() => handleTogglePurchase(item.id)}
                  className="text-gray-600 hover:text-gray-900"
                >
                  撤销
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* 提示 */}
      <div className="mt-8 p-4 bg-blue-50 rounded-lg">
        <h3 className="font-medium text-blue-900 mb-2">提示</h3>
        <p className="text-sm text-blue-700">
          在配方页面，您可以点击"添加到购物清单"来快速生成需要购买的材料列表。
        </p>
      </div>
    </div>
  );
};

export default ShoppingListPage;