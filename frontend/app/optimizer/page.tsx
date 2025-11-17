'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import CardInputForm from '@/components/CardInputForm';
import MultiCardComparisonTable from '@/components/MultiCardComparisonTable';
import SavingsSimulationChart from '@/components/SavingsSimulationChart';
import OfferCard from '@/components/OfferCard';
import DetailedSavingsModal from '@/components/DetailedSavingsModal';
import { LoadingSkeleton } from '@/components/LoadingSkeleton';
import { useAppStore } from '@/lib/store';
import { recommendCards } from '@/lib/api-client';
import toast from 'react-hot-toast';
import { Button } from '@/components/ui/button';
import { Save, Info } from 'lucide-react';
import type { CardRecommendation } from '@/lib/types';

export default function OptimizerPage() {
  const {
    spend,
    recommendations,
    setRecommendations,
    isLoading,
    setIsLoading,
    saveSimulation,
  } = useAppStore();

  const [selectedCard, setSelectedCard] = useState<CardRecommendation | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleRecommend = async () => {
    const totalSpend = Object.values(spend).reduce((a, b) => a + b, 0);
    if (totalSpend === 0) {
      toast.error('Please enter at least one spending category');
      return;
    }

    setIsLoading(true);
    try {
      const response = await recommendCards({ spend });
      setRecommendations(response.recommendations);
      toast.success('Recommendations generated!');
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to get recommendations';
      toast.error(message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSave = () => {
    if (!recommendations) return;
    saveSimulation({
      spend,
      recommendations,
    });
    toast.success('Simulation saved!');
  };

  const handleViewDetails = (card: CardRecommendation) => {
    setSelectedCard(card);
    setIsModalOpen(true);
  };

  return (
    <div className="min-h-screen py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-12"
        >
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Credit Card Optimizer
          </h1>
          <p className="text-xl text-gray-300 max-w-2xl mx-auto">
            Enter your monthly spending to find the best credit cards for you
          </p>
        </motion.div>

        <div className="mb-8">
          <CardInputForm onSubmit={handleRecommend} />
          <div className="mt-6 flex justify-center">
          </div>
        </div>

        {isLoading && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            {[1, 2, 3].map((i) => (
              <LoadingSkeleton key={i} />
            ))}
          </div>
        )}

        {recommendations && !isLoading && (
          <>
            <div className="mb-6 flex justify-end">
              <Button
                onClick={handleSave}
                variant="outline"
                className="border-purple-500/50 hover:bg-purple-500/10"
              >
                <Save className="w-4 h-4 mr-2" />
                Save Simulation
              </Button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
              {recommendations.map((card, index) => (
                <div key={card.card_name} className="relative">
                  <OfferCard
                    recommendation={card}
                    isBest={index === 0}
                    index={index}
                  />
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={() => handleViewDetails(card)}
                    className="absolute top-4 right-4 border-purple-500/50 hover:bg-purple-500/10"
                  >
                    <Info className="w-4 h-4 mr-1" />
                    Details
                  </Button>
                </div>
              ))}
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
              <MultiCardComparisonTable
                recommendations={recommendations}
                bestCard={recommendations[0]}
                onViewDetails={handleViewDetails}
              />
              <SavingsSimulationChart recommendations={recommendations} />
            </div>
          </>
        )}

        <DetailedSavingsModal
          card={selectedCard}
          isOpen={isModalOpen}
          onClose={() => setIsModalOpen(false)}
        />
      </div>
    </div>
  );
}
