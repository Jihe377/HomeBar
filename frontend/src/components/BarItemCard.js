import React from 'react';

const BarItemCard = ({ item, onEdit, onDelete }) => {
  const getCategoryColor = (category) => {
    const colors = {
      spirit: 'bg-red-100 text-red-800',
      liqueur: 'bg-purple-100 text-purple-800',
      wine: 'bg-pink-100 text-pink-800',
      beer: 'bg-amber-100 text-amber-800',
      mixer: 'bg-blue-100 text-blue-800',
      fruit: 'bg-green-100 text-green-800',
      herb: 'bg-emerald-100 text-emerald-800',
      other: 'bg-gray-100 text-gray-800',
    };
    return colors[category] || colors.other;
  };

  const getCategoryLabel = (category) => {
    const labels = {
      spirit: '基酒',
      liqueur: '利口酒',
      wine: '葡萄酒',
      beer: '啤酒',
      mixer: '调酒饮料',
      fruit: '水果',
      herb: '香草',
      other: '其他',
    };
    return labels[category] || '其他';
  };

  const volumePercentage = item.volume > 0 ? (item.currentVolume / item.volume) * 100 : 0;

  return (
    <div className="card hover:shadow-lg transition-shadow">
      <div className="flex justify-between items-start mb-4">
        <div>
          <h3 className="text-xl font-bold text-gray-900">{item.name}</h3>
          <p className="text-gray-600">{item.brand}</p>
        </div>
        <span className={`px-3 py-1 rounded-full text-sm font-medium ${getCategoryColor(item.category)}`}>
          {getCategoryLabel(item.category)}
        </span>
      </div>

      {/* 容量条 */}
      <div className="mb-4">
        <div className="flex justify-between text-sm text-gray-600 mb-1">
          <span>剩余容量</span>
          <span>{item.currentVolume}ml / {item.volume}ml</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-2">
          <div
            className={`h-2 rounded-full ${
              volumePercentage > 50 ? 'bg-green-500' :
              volumePercentage > 20 ? 'bg-yellow-500' : 'bg-red-500'
            }`}
            style={{ width: `${Math.min(volumePercentage, 100)}%` }}
          />
        </div>
      </div>

      {/* 详细信息 */}
      <div className="space-y-2 text-sm text-gray-600">
        {item.abv > 0 && (
          <div className="flex justify-between">
            <span>酒精度</span>
            <span className="font-medium">{item.abv}%</span>
          </div>
        )}
        <div className="flex justify-between">
          <span>状态</span>
          <span className={`font-medium ${item.isAvailable ? 'text-green-600' : 'text-red-600'}`}>
            {item.isAvailable ? '可用' : '已用完'}
          </span>
        </div>
      </div>

      {/* 操作按钮 */}
      <div className="flex justify-end space-x-2 mt-4 pt-4 border-t">
        <button
          onClick={() => onEdit(item.id)}
          className="px-3 py-1 text-sm text-gray-600 hover:text-gray-900"
        >
          编辑
        </button>
        <button
          onClick={() => onDelete(item.id)}
          className="px-3 py-1 text-sm text-red-600 hover:text-red-900"
        >
          删除
        </button>
      </div>
    </div>
  );
};

export default BarItemCard;