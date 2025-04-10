import { useState, useEffect } from 'react';
import { format } from 'date-fns';
import { PieChart, DollarSign, TrendingUp } from 'lucide-react';
import { getEntries } from '../api';
import { useAuth } from '../context/AuthContext';
import { BudgetEntry } from '../types';

export function Dashboard() {
  const [entries, setEntries] = useState<BudgetEntry[]>([]);
  const { userId } = useAuth();

  useEffect(() => {
    if (userId) {
      getEntries(userId).then(setEntries).catch(console.error);
    }
  }, [userId]);

  const totalSpent = entries.reduce((sum, entry) => sum + entry.amount, 0);
  
  const categoryTotals = entries.reduce((acc, entry) => {
    acc[entry.category] = (acc[entry.category] || 0) + entry.amount;
    return acc;
  }, {} as Record<string, number>);

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-sm">
          <div className="flex items-center">
            <DollarSign className="h-8 w-8 text-green-500" />
            <h3 className="ml-2 text-lg font-semibold text-gray-900">Total Spent</h3>
          </div>
          <p className="mt-2 text-3xl font-bold text-gray-900">${totalSpent.toFixed(2)}</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow-sm">
          <div className="flex items-center">
            <PieChart className="h-8 w-8 text-blue-500" />
            <h3 className="ml-2 text-lg font-semibold text-gray-900">Categories</h3>
          </div>
          <p className="mt-2 text-3xl font-bold text-gray-900">{Object.keys(categoryTotals).length}</p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-sm">
          <div className="flex items-center">
            <TrendingUp className="h-8 w-8 text-purple-500" />
            <h3 className="ml-2 text-lg font-semibold text-gray-900">Entries</h3>
          </div>
          <p className="mt-2 text-3xl font-bold text-gray-900">{entries.length}</p>
        </div>
      </div>

      <div className="bg-white shadow-sm rounded-lg overflow-hidden">
        <div className="px-4 py-5 sm:px-6">
          <h3 className="text-lg font-medium leading-6 text-gray-900">Recent Transactions</h3>
        </div>
        <div className="border-t border-gray-200">
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Category</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {entries.map((entry) => (
                  <tr key={entry.id}>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {format(new Date(entry.date), 'MMM d, yyyy')}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{entry.category}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${entry.amount.toFixed(2)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
