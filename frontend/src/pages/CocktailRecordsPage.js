import React from 'react';

const CocktailRecordsPage = () => {
  const records = [
    { id: 1, recipeName: '金汤力', date: '2024-01-15', rating: 5, notes: '完美比例' },
    { id: 2, recipeName: '莫吉托', date: '2024-01-10', rating: 4, notes: '薄荷可以再多一点' },
    { id: 3, recipeName: '古典鸡尾酒', date: '2024-01-05', rating: 3, notes: '威士忌味道太重' },
  ];

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">调酒记录</h1>
          <p className="text-gray-600 mt-2">记录您的每一次调酒体验</p>
        </div>
        <button className="btn-primary flex items-center">
          <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          添加记录
        </button>
      </div>

      <div className="space-y-4">
        {records.map((record) => (
          <div key={record.id} className="card">
            <div className="flex justify-between items-start">
              <div>
                <h3 className="text-lg font-bold text-gray-900">{record.recipeName}</h3>
                <p className="text-gray-600 text-sm mt-1">{record.date}</p>
                {record.notes && (
                  <p className="mt-2 text-gray-700">{record.notes}</p>
                )}
              </div>
              <div className="flex items-center">
                {[...Array(5)].map((_, i) => (
                  <svg
                    key={i}
                    className={`w-5 h-5 ${i < record.rating ? 'text-yellow-400' : 'text-gray-300'}`}
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>

      {records.length === 0 && (
        <div className="text-center py-12">
          <svg className="w-16 h-16 mx-auto text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <h3 className="mt-4 text-lg font-medium text-gray-900">暂无调酒记录</h3>
          <p className="mt-2 text-gray-600">记录您的第一次调酒体验吧！</p>
          <button className="mt-4 btn-primary">
            添加记录
          </button>
        </div>
      )}
    </div>
  );
};

export default CocktailRecordsPage;